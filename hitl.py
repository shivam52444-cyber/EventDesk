"""
hitl.py - human-in-the-loop bridge.

Agents and flow steps are plain blocking Python, so when they need the user they call `hitl.ask(...)`.
  * Under the API (run_manager binds a session): the question is published to the run's SSE stream
    and the calling thread sleeps until POST /runs/{id}/answer delivers a reply (or the timeout hits).
  * Without a session (CLI, evaluation.py): falls back to the old console behaviour, with the same
    "[AGENT QUESTION]" print format that evaluation.py's SimulatedHuman already understands.
"""
from __future__ import annotations

import contextvars
import os
import threading
import time
import uuid
from typing import Callable, Optional, Sequence

DEFAULT_TIMEOUT_S = int(os.getenv("HITL_TIMEOUT_S", "300"))
TIMEOUT_REPLY = "User did not respond in time. Proceed with safe defaults."
FALLBACK_REPLY = "User did not provide a valid safe answer after 3 attempts. Proceed with safe defaults."


class AskSession:
    """One per run. `ask` is called from the flow thread, `submit` from the API thread."""

    def __init__(self, publish: Callable[[str, dict], None], set_status: Callable[[str], None]):
        self._cond = threading.Condition()
        self._publish, self._set_status = publish, set_status
        self.pending: Optional[dict] = None
        self._answer: Optional[str] = None

    def ask(self, text: str, kind: str = "text", options: Optional[Sequence[str]] = None,
            channel: str = "agent", timeout: Optional[float] = None) -> str:
        timeout = DEFAULT_TIMEOUT_S if timeout is None else timeout
        q = {"id": uuid.uuid4().hex[:8], "text": text, "kind": kind, "options": list(options or []),
             "channel": channel, "timeout_s": timeout}
        with self._cond:
            self.pending, self._answer = q, None
        self._set_status("waiting_for_input")
        self._publish("question", q)
        deadline = time.monotonic() + timeout
        with self._cond:
            while self._answer is None:
                left = deadline - time.monotonic()
                if left <= 0:
                    break
                self._cond.wait(left)
            answer, self._answer, self.pending = self._answer, None, None
        self._set_status("running")
        if answer is None:
            self._publish("question_timeout", {"id": q["id"]})
            return TIMEOUT_REPLY
        self._publish("answer_received", {"id": q["id"]})
        return answer

    def submit(self, question_id: str, answer: str) -> str:
        """-> 'ok' | 'no_pending' | 'stale'"""
        with self._cond:
            if self.pending is None:
                return "no_pending"
            if self.pending["id"] != question_id or self._answer is not None:
                return "stale"  # wrong question, or a double submit before the agent thread woke up
            self._answer = answer
            self._cond.notify_all()
            return "ok"


_session_var: contextvars.ContextVar = contextvars.ContextVar("hitl_session", default=None)
_active: Optional[AskSession] = None  # fallback: the flow may run in a thread that did not inherit the context


def bind(session: AskSession) -> None:
    global _active
    _session_var.set(session)
    _active = session


def unbind() -> None:
    global _active
    _session_var.set(None)
    _active = None


def current() -> Optional[AskSession]:
    return _session_var.get() or _active


def console_ask(question: str, channel: str = "agent") -> str:
    import gaurdrails  # looked up at call time so evaluation.py's guardrail stub still applies
    tag = "AGENT QUESTION" if channel == "agent" else "FLOW QUESTION"
    for _ in range(3):
        print(f"\n🤖 [{tag}]: {question}")
        reply = input("👤 [YOUR ANSWER]: ").strip()
        if not reply:
            print("⚠️ [Guardrail]: reply can't be empty. Please try again.")
            continue
        try:
            return gaurdrails.validate_with_lakera(reply, "Human Reply")
        except ValueError as e:
            print(f"\n{e}\n⚠️ That looks unsafe. Please provide a safe and valid answer.")
    return FALLBACK_REPLY


def ask(question: str, *, kind: str = "text", options: Optional[Sequence[str]] = None, channel: str = "agent") -> str:
    """channel: 'agent' for questions raised by an agent tool, 'flow' for questions raised by a flow step."""
    s = current()
    if s is None:
        return console_ask(question, channel)
    return s.ask(question, kind=kind, options=options, channel=channel)
