from __future__ import annotations

import asyncio
import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

import run_manager as rm
from database import load_run_from_db, list_recent_runs

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI(title="Event Management Planner", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DEMO_HTML = Path(__file__).resolve().parent / "demo.html"


class CreateRunRequest(BaseModel):
    event_topic: str
    description: str
    city: str
    guests: int
    total_budget: int


class AnswerRequest(BaseModel):
    question_id: str
    answer: str


def _get_run(run_id: str) -> rm.Run:
    run = rm.store.get(run_id)
    if run is None:
        raise HTTPException(404, f"Unknown run '{run_id}'.")
    return run


@app.get("/", include_in_schema=False)
def index():
    if DEMO_HTML.exists():
        return FileResponse(DEMO_HTML)
    return {"message": "POST /runs to start planning."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/runs")
def list_runs():
    return {"runs": list_recent_runs(20)}


@app.post("/runs", status_code=202)
async def create_run(body: CreateRunRequest):
    loop = asyncio.get_running_loop()
    try:
        cleaned = await loop.run_in_executor(None, rm.validate_inputs, body.model_dump())
    except ValueError as e:
        raise HTTPException(422, str(e))
    except RuntimeError as e:
        raise HTTPException(503, str(e))
    run = rm.submit(cleaned)
    return {
        "run_id": run.id,
        "status": run.status,
        "events_url": f"/runs/{run.id}/events",
        "answer_url": f"/runs/{run.id}/answer",
    }


@app.get("/runs/{run_id}")
def get_run(run_id: str):
    run = rm.store.get(run_id)
    if run is not None:
        return run.snapshot()
    # RAM mein nahi mila (server restart ke baad) toh SQLite DB se load karein
    db_snap = load_run_from_db(run_id)
    if db_snap is not None:
        return db_snap
    raise HTTPException(404, f"Unknown run '{run_id}'.")


@app.get("/runs/{run_id}/events")
async def stream_events(run_id: str, request: Request, after: int = 0):
    run = _get_run(run_id)
    hdr = request.headers.get("last-event-id")
    if hdr and hdr.isdigit():
        after = max(after, int(hdr))
    return StreamingResponse(
        rm.sse_events(run, after=after),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.post("/runs/{run_id}/answer")
async def post_answer(run_id: str, body: AnswerRequest):
    run = _get_run(run_id)
    if run.finished:
        raise HTTPException(409, "This run has already finished.")
    loop = asyncio.get_running_loop()
    try:
        cleaned = await loop.run_in_executor(None, rm.validate_answer, body.answer)
    except ValueError as e:
        raise HTTPException(422, str(e))
    except RuntimeError as e:
        raise HTTPException(503, str(e))
    outcome = run.session.submit(body.question_id, cleaned)
    if outcome == "no_pending":
        raise HTTPException(409, "This run is not waiting for an answer.")
    if outcome == "stale":
        raise HTTPException(409, "That question was already answered or timed out.")
    return {"status": "accepted", "question_id": body.question_id}
