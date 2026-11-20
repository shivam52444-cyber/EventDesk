"""
api.py - FastAPI front door for the event planner.

  POST /runs                  validate input (incl. Lakera) and start a run          -> 202 {run_id, ...}
  GET  /runs/{id}/events      Server-Sent Events: progress, thinking, tools, partial results, questions
  POST /runs/{id}/answer      reply to a question the agents asked
  GET  /runs/{id}             snapshot (status, partial results, pending question) for page refresh / polling
  GET  /                      small demo page (demo.html) to try it in a browser

Run with ONE worker (state lives in this process until the database step):
  uvicorn api:app --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import json
import logging
import os
import sys
from pathlib import Path
from typing import Optional

if sys.platform.startswith("win"):  # same hang fix as main.py
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field, ValidationError

import run_manager as rm

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format="%(asctime)s %(levelname)s %(name)s: %(message)s")
HERE = Path(__file__).resolve().parent

app = FastAPI(title="Event planner API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:8501,http://localhost:3000").split(",") if o.strip()],
    allow_methods=["*"], allow_headers=["*"])


class PlanRequest(BaseModel):
    event_topic: str = Field(min_length=3, max_length=120, examples=["Marriage engagement"])
    description: str = Field(min_length=10, max_length=1000, examples=["Beachside party with family and friends"])
    city: str = Field(min_length=1, max_length=80, examples=["Goa"])
    guests: int = Field(gt=0, le=50000, examples=[300])
    total_budget: int = Field(ge=5000, examples=[1000000], description="Total budget in INR")


class AnswerRequest(BaseModel):
    question_id: str
    answer: str = Field(min_length=1, max_length=500)


def _get_run(run_id: str) -> rm.Run:
    run = rm.store.get(run_id)
    if run is None:
        raise HTTPException(404, "Run not found. It may have expired.")
    return run


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/runs", status_code=202)
async def create_run(req: PlanRequest):
    try:
        inputs = await run_in_threadpool(rm.validate_inputs, req.model_dump())
    except ValidationError as e:
        raise HTTPException(422, detail=json.loads(e.json()))
    except RuntimeError:
        raise HTTPException(503, "The safety check is unavailable. Please try again shortly.")
    run = rm.submit(inputs)
    base = f"/runs/{run.id}"
    return {"run_id": run.id, "status": run.status, "status_url": base, "events_url": f"{base}/events", "answer_url": f"{base}/answer"}


@app.get("/runs/{run_id}")
def get_run(run_id: str):
    return _get_run(run_id).snapshot()


@app.get("/runs/{run_id}/events")
async def run_events(run_id: str, request: Request, after: int = Query(0, ge=0),
                     last_event_id: Optional[str] = Header(default=None)):
    run = _get_run(run_id)
    cursor = after
    if last_event_id and last_event_id.isdigit():  # EventSource sends this automatically when it reconnects
        cursor = max(cursor, int(last_event_id))

    async def gen():
        async for chunk in rm.sse_events(run, cursor):
            if await request.is_disconnected():
                break
            yield chunk

    return StreamingResponse(gen(), media_type="text/event-stream", headers={
        "Cache-Control": "no-cache, no-transform", "X-Accel-Buffering": "no", "Connection": "keep-alive"})


@app.post("/runs/{run_id}/answer")
async def answer(run_id: str, body: AnswerRequest):
    run = _get_run(run_id)
    if run.session.pending is None:
        raise HTTPException(409, "The planner is not waiting for an answer right now.")
    try:
        clean = await run_in_threadpool(rm.validate_answer, body.answer)
    except ValueError:
        raise HTTPException(422, "That answer was empty, too long, or flagged as unsafe. Please rephrase it.")
    except RuntimeError:
        raise HTTPException(503, "The safety check is unavailable. Please try again shortly.")
    outcome = run.session.submit(body.question_id, clean)
    if outcome != "ok":
        raise HTTPException(409, "That question was already answered or has expired.")
    return {"accepted": True}


@app.get("/", include_in_schema=False)
def demo_page():
    return FileResponse(HERE / "demo.html")
