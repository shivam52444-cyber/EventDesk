"""
run_manager.py - everything between the HTTP layer and the CrewAI flow.

  Run             one planner execution: ordered event log + status + partial/final results
  RunStore        in-memory registry with TTL pruning (swap for Postgres/SQLite later)
  FrameBridge     turns CrewAI stream frames into clean API events (progress, thinking, tools)
  ThoughtFilter   keeps only the agent's 'Thought:' text out of ReAct output (hides Action/Final Answer JSON)
  sse_events      async generator that replays + tails a run's events, resumable via Last-Event-ID
  execute/submit  runs flows concurrently across multiple worker threads (each run instantiates fresh agents/tools)
"""
from __future__ import annotations
from database import save_run_snapshot
import asyncio
import contextvars
import json
import logging
import re
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional

import hitl
log = logging.getLogger("planner")

STAGES = {
    "Venue Coordinator": "venue",
    "Logistics Manager": "logistics",
    "Marketing and Communications Agent": "marketing",
}
STEP_LABELS = {  # flow method -> (key, label shown to the user)
    "find_venue_step": ("venue", "Finding a venue"),
    "ask_human_catering": ("catering", "Waiting for your catering choice"),
    "run_logistics_step": ("logistics", "Planning catering and equipment"),
    "run_marketing_step": ("marketing", "Writing the invitation and posts"),
}

_ACTIVE_RUN_VAR: contextvars.ContextVar[Optional["Run"]] = contextvars.ContextVar("active_run", default=None)


# ---------------------------------------------------------------------------------------------
# Run + store
# ---------------------------------------------------------------------------------------------
class Run:
    def __init__(self, run_id: str, inputs: dict):
        self.id, self.inputs = run_id, inputs
        self.created = time.time()
        self.status = "queued"
        self.events: List[dict] = []
        self.lock = threading.RLock()
        self.subs: List[tuple] = []
        self.finished = False
        self.stage = "outside"
        self.partial: Dict[str, Any] = {}
        self.attempts: Dict[str, int] = {}
        self.result: Optional[dict] = None
        self.error: Optional[dict] = None
        self.usage: Dict[str, Any] = {"total_tokens": 0, "prompt_tokens": 0, "completion_tokens": 0, "by_stage": {}}
        self.marks: Dict[str, float] = {}
        self.t0: Optional[float] = None
        self.session = hitl.AskSession(self.publish, self.set_status)

    def publish(self, type_: str, data: Optional[dict] = None) -> None:
        if type_ == "thinking":
            self.mark("first_thought")
        elif type_ == "stage_result":
            self.mark("first_result")
        with self.lock:
            ev = {"id": len(self.events) + 1, "type": type_, "ts": round(time.time(), 3), "data": data or {}}
            self.events.append(ev)
        self._wake()

    def _wake(self) -> None:
        for loop, evt in list(self.subs):
            try:
                loop.call_soon_threadsafe(evt.set)
            except RuntimeError:
                pass

    def set_status(self, status: str) -> None:
        with self.lock:
            self.status = status
        self.publish("status", {"status": status})

    def mark(self, name: str) -> None:
        if self.t0 is not None and name not in self.marks:
            self.marks[name] = round(time.perf_counter() - self.t0, 2)

    def record_stage(self, stage: str, data: Optional[dict], tokens: dict, dur: float) -> None:
        with self.lock:
            self.attempts[stage] = self.attempts.get(stage, 0) + 1
            if data is not None:
                self.partial[stage] = data
            u = self.usage
            for k in ("total_tokens", "prompt_tokens", "completion_tokens"):
                u[k] += int(tokens.get(k, 0) or 0)
            u["by_stage"][stage] = u["by_stage"].get(stage, 0) + int(tokens.get("total_tokens", 0) or 0)
            attempt = self.attempts[stage]
        self.publish("stage_result", {"stage": stage, "attempt": attempt, "data": data, "seconds": round(dur, 2)})
        save_run_snapshot(self.snapshot())
    def finish(self, ok: bool, result: Optional[dict] = None, error: Optional[dict] = None) -> None:
        with self.lock:
            self.result, self.error = result, error
        total = round(time.perf_counter() - self.t0, 2) if self.t0 else None
        if ok:
            self.publish("result", {"plan": result})
        else:
            self.publish("error", error or {})
        self.publish("usage", {**self.usage, "seconds_total": total, "seconds_to": dict(self.marks)})
        self.set_status("succeeded" if ok else "failed")
        self.publish("done", {"ok": ok})
        with self.lock:
            self.finished = True
        self._wake()
        save_run_snapshot(self.snapshot())

    def snapshot(self) -> dict:
        with self.lock:
            return {
                "run_id": self.id,
                "status": self.status,
                "created": self.created,
                "inputs": self.inputs,
                "pending_question": self.session.pending,
                "partial": dict(self.partial),
                "result": self.result,
                "error": self.error,
                "usage": self.usage,
                "last_event_id": len(self.events),
            }


class RunStore:
    def __init__(self, ttl_s: int = 3600, max_runs: int = 200):
        self._runs: Dict[str, Run] = {}
        self._lock = threading.Lock()
        self.ttl_s, self.max_runs = ttl_s, max_runs

    def create(self, inputs: dict) -> Run:
        run = Run(uuid.uuid4().hex[:12], inputs)
        with self._lock:
            self._prune()
            self._runs[run.id] = run
        return run

    def get(self, run_id: str) -> Optional[Run]:
        with self._lock:
            return self._runs.get(run_id)

    def unfinished_before(self, run: Run) -> int:
        with self._lock:
            return sum(1 for r in self._runs.values() if r is not run and not r.finished and r.created <= run.created)

    def _prune(self) -> None:
        now = time.time()
        done = sorted((r for r in self._runs.values() if r.finished), key=lambda r: r.created)
        for r in done:
            if now - r.created > self.ttl_s or len(self._runs) > self.max_runs:
                self._runs.pop(r.id, None)


store = RunStore()


# ---------------------------------------------------------------------------------------------
# SSE
# ---------------------------------------------------------------------------------------------
async def sse_events(run: Run, after: int = 0, keepalive_s: float = 15.0):
    loop, wake = asyncio.get_running_loop(), asyncio.Event()
    sub = (loop, wake)
    with run.lock:
        run.subs.append(sub)
    cursor = after
    try:
        yield "retry: 3000\n\n"
        while True:
            wake.clear()
            with run.lock:
                new, done = run.events[cursor:], run.finished
            for ev in new:
                cursor = ev["id"]
                yield f"id: {ev['id']}\ndata: {json.dumps(ev, ensure_ascii=False, default=str)}\n\n"
            if done and not new:
                return
            try:
                await asyncio.wait_for(wake.wait(), timeout=keepalive_s)
            except asyncio.TimeoutError:
                yield ": keepalive\n\n"
    finally:
        with run.lock:
            if sub in run.subs:
                run.subs.remove(sub)


# ---------------------------------------------------------------------------------------------
# Agent "thinking"
# ---------------------------------------------------------------------------------------------
_THOUGHT_PREFIX = re.compile(r"\s*Thought:\s*")


class ThoughtFilter:
    STOPS = ("Action Input:", "Action:", "Final Answer:")
    HOLD = max(len(s) for s in STOPS) - 1

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.buf, self.sent, self.stopped, self.started = "", 0, False, False

    def _end(self, final: bool) -> int:
        cuts = [i for i in (self.buf.find(s) for s in self.STOPS) if i >= 0]
        if cuts:
            self.stopped = True
            return min(cuts)
        return len(self.buf) if final else max(self.sent, len(self.buf) - self.HOLD)

    def _take(self, end: int) -> str:
        if not self.started:
            m = _THOUGHT_PREFIX.match(self.buf)
            if m:
                self.sent = max(self.sent, m.end())
        end = max(end, self.sent)
        out = self.buf[self.sent:end]
        self.sent = end
        if self.stopped:
            out = out.rstrip()
        if out:
            self.started = True
        return out

    def feed(self, chunk: str) -> str:
        if self.stopped or not chunk:
            return ""
        self.buf += chunk
        return self._take(self._end(False))

    def flush(self) -> str:
        if self.stopped:
            return ""
        out = self._take(self._end(True))
        self.stopped = True
        return out


class ThinkBatcher:
    def __init__(self, emit, min_interval: float = 0.08):
        self.emit, self.min_interval = emit, min_interval
        self.stage, self.source, self.buf, self.last = "", "thought", "", 0.0

    def add(self, stage: str, source: str, text: str) -> None:
        if not text:
            return
        if (stage, source) != (self.stage, self.source):
            self.flush()
            self.stage, self.source = stage, source
        self.buf += text
        if time.monotonic() - self.last >= self.min_interval:
            self.flush()

    def flush(self) -> None:
        if self.buf:
            self.emit("thinking", {"stage": self.stage, "source": self.source, "delta": self.buf})
            self.buf = ""
        self.last = time.monotonic()


def _event_dict(frame: Any) -> dict:
    e = getattr(frame, "event", None)
    if e is None:
        e = getattr(frame, "data", None)
    if isinstance(e, dict):
        return e
    if hasattr(e, "model_dump"):
        try:
            return e.model_dump()
        except Exception:
            return {}
    return dict(vars(e)) if hasattr(e, "__dict__") else {}


def _short(v: Any, n: int = 300) -> str:
    return (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, default=str))[:n] if v is not None else ""


class FrameBridge:
    def __init__(self, run: Run):
        self.run, self.filter = run, ThoughtFilter()
        self.batch = ThinkBatcher(run.publish)

    def stage_for(self, ev: dict) -> str:
        return STAGES.get(ev.get("agent_role")) or self.run.stage

    def handle(self, frame: Any) -> None:
        channel, typ = str(getattr(frame, "channel", "")), str(getattr(frame, "type", "")).lower()
        ev, content = _event_dict(frame), getattr(frame, "content", "") or ""
        if channel == "llm":
            self._llm(typ, ev, content)
        elif channel == "tools":
            self.batch.flush()
            self._tool(typ, ev)
        elif channel == "flow":
            self.batch.flush()
            self._flow(typ, ev)

    def _llm(self, typ: str, ev: dict, content: str) -> None:
        stage = self.stage_for(ev)
        if "thinking" in typ:
            self.batch.add(stage, "reasoning", content)
        elif "chunk" in typ:
            self.batch.add(stage, "thought", self.filter.feed(content))
        elif "started" in typ:
            self.filter.reset()
        elif "completed" in typ or "failed" in typ:
            self.batch.add(stage, "thought", self.filter.flush())
            if self.filter.started:
                self.batch.add(stage, "thought", "\n\n")
            self.batch.flush()

    def _tool(self, typ: str, ev: dict) -> None:
        stage, name = self.stage_for(ev), str(ev.get("tool_name") or "")
        if "error" in typ:
            self.run.publish("tool_error", {"stage": stage, "tool": name, "error": _short(ev.get("error"))})
        elif "started" in typ:
            self.run.publish("tool_started", {"stage": stage, "tool": name, "args": _short(ev.get("tool_args"))})
        elif "finished" in typ:
            self.run.publish("tool_finished", {"stage": stage, "tool": name, "preview": _short(ev.get("output"))})

    def _flow(self, typ: str, ev: dict) -> None:
        name = ev.get("method_name")
        if name not in STEP_LABELS:
            return
        key, label = STEP_LABELS[name]
        status = "started" if "started" in typ else "finished" if "finished" in typ else "failed" if "fail" in typ else None
        if status:
            self.run.publish("step", {"step": key, "label": label, "status": status})


_HOOKED = False
_HOOK_LOCK = threading.Lock()


def install_hooks() -> None:
    global _HOOKED
    if _HOOKED:
        return
    with _HOOK_LOCK:
        if _HOOKED:
            return
        from crewai import Crew
        orig_sync = Crew.kickoff
        orig_async = Crew.akickoff

        def _on_start(self):
            run = _ACTIVE_RUN_VAR.get()
            if run is None:
                return None, None, None
            role = self.agents[0].role if getattr(self, "agents", None) else "?"
            stage = STAGES.get(role, role)
            run.stage = stage
            run.publish("stage_started", {"stage": stage, "role": role})
            return run, stage, time.perf_counter()

        def _on_end(run, stage, t0, out):
            if run is None:
                return
            if hasattr(out, "result") and not hasattr(out, "pydantic"):
                out = out.result
            p = getattr(out, "pydantic", None)
            data = p.model_dump() if p is not None and hasattr(p, "model_dump") else None
            u = getattr(out, "token_usage", None)
            tokens = {}
            if u is not None:
                get = (lambda k: u.get(k, 0)) if isinstance(u, dict) else (lambda k: getattr(u, k, 0))
                tokens = {k: get(k) for k in ("total_tokens", "prompt_tokens", "completion_tokens")}
            run.record_stage(stage, data, tokens, time.perf_counter() - t0)

        def sync_wrapper(self, *args, **kwargs):
            run, stage, t0 = _on_start(self)
            try:
                out = orig_sync(self, *args, **kwargs)
            except BaseException as e:
                if run:
                    run.publish("stage_failed", {"stage": stage, "error": f"{type(e).__name__}: {e}"[:300]})
                raise
            _on_end(run, stage, t0, out)
            return out

        async def async_wrapper(self, *args, **kwargs):
            run, stage, t0 = _on_start(self)
            try:
                out = await orig_async(self, *args, **kwargs)
            except BaseException as e:
                if run:
                    run.publish("stage_failed", {"stage": stage, "error": f"{type(e).__name__}: {e}"[:300]})
                raise
            _on_end(run, stage, t0, out)
            return out

        Crew.kickoff = sync_wrapper
        Crew.akickoff = async_wrapper
        _HOOKED = True


def _public_error(e: BaseException) -> dict:
    name = type(e).__name__
    if name == "ValidationError":
        return {"code": "invalid_input", "message": "The event details were rejected."}
    if name in ("RuntimeError",) and "Guardrail service" in str(e):
        return {"code": "guardrail_unavailable", "message": "The safety check is unavailable. Please try again shortly."}
    return {"code": "planner_failed", "message": "The planner failed while building your plan. Please try again."}


async def execute_async(run: Run) -> None:
    token = _ACTIVE_RUN_VAR.set(run)
    hitl.bind(run.session, run.id)
    run.t0 = time.perf_counter()
    run.set_status("running")
    bridge = FrameBridge(run)
    try:
        install_hooks()
        from flow import EventManagementFlow
        flow = EventManagementFlow()
        flow_inputs = {**run.inputs, "run_id": run.id}

        # CrewAI 1.x mein stream_events() sync generator hota hai; thread mein bridge chala kar async result lein
        if hasattr(flow, "stream_events"):
            def _run_stream():
                with flow.stream_events(inputs=flow_inputs) as stream:
                    for frame in stream:
                        try:
                            bridge.handle(frame)
                        except Exception:
                            log.exception("frame bridge error (run %s)", run.id)
                    return stream.result

            result = await asyncio.to_thread(_run_stream)
        else:
            result = await flow.kickoff_async(inputs=flow_inputs)

        bridge.batch.flush()
        if not isinstance(result, dict):
            raise RuntimeError(f"flow returned {type(result).__name__}, expected a plan dict")
        run.finish(True, result=json.loads(json.dumps(result, default=str)))
    except BaseException as e:  # noqa: BLE001
        log.exception("run %s failed", run.id)
        bridge.batch.flush()
        run.finish(False, error=_public_error(e))
    finally:
        hitl.unbind(run.id)
        _ACTIVE_RUN_VAR.reset(token)


def submit(inputs: dict) -> Run:
    run = store.create(inputs)
    run.set_status("queued")
    run.publish("queued", {"position": store.unfinished_before(run)})
    asyncio.create_task(execute_async(run))
    return run


def validate_inputs(data: dict) -> dict:
    from sstate import EventState
    st = EventState(**data)
    return {k: getattr(st, k) for k in ("event_topic", "description", "city", "guests", "total_budget")}


def validate_answer(text: str) -> str:
    text = (text or "").strip()
    if not text:
        raise ValueError("Answer cannot be empty.")
    if len(text) > 500:
        raise ValueError("Answer is too long (500 characters max).")
    import gaurdrails
    return gaurdrails.validate_with_lakera(text, "Human Reply", use_cache=True)
