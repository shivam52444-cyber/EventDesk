import json
import sqlite3
import threading
import time
from pathlib import Path
from typing import Any, List, Optional

DB_PATH = Path(__file__).resolve().parent / "event_planner.db"
_DB_LOCK = threading.Lock()


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _DB_LOCK, _conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                run_id TEXT PRIMARY KEY,
                status TEXT NOT NULL,
                created REAL NOT NULL,
                inputs_json TEXT NOT NULL,
                partial_json TEXT,
                result_json TEXT,
                error_json TEXT,
                usage_json TEXT
            )
        """)


def save_run_snapshot(snap: dict) -> None:
    with _DB_LOCK, _conn() as conn:
        conn.execute("""
            INSERT INTO runs (run_id, status, created, inputs_json, partial_json, result_json, error_json, usage_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(run_id) DO UPDATE SET
                status = excluded.status,
                partial_json = excluded.partial_json,
                result_json = excluded.result_json,
                error_json = excluded.error_json,
                usage_json = excluded.usage_json
        """, (
            snap["run_id"],
            snap["status"],
            snap["created"],
            json.dumps(snap["inputs"], ensure_ascii=False, default=str),
            json.dumps(snap.get("partial") or {}, ensure_ascii=False, default=str),
            json.dumps(snap.get("result"), ensure_ascii=False, default=str) if snap.get("result") is not None else None,
            json.dumps(snap.get("error"), ensure_ascii=False, default=str) if snap.get("error") is not None else None,
            json.dumps(snap.get("usage") or {}, ensure_ascii=False, default=str),
        ))


def load_run_from_db(run_id: str) -> Optional[dict]:
    with _DB_LOCK, _conn() as conn:
        row = conn.execute("SELECT * FROM runs WHERE run_id = ?", (run_id,)).fetchone()
        if not row:
            return None
        return {
            "run_id": row["run_id"],
            "status": row["status"],
            "created": row["created"],
            "inputs": json.loads(row["inputs_json"]),
            "pending_question": None,
            "partial": json.loads(row["partial_json"]) if row["partial_json"] else {},
            "result": json.loads(row["result_json"]) if row["result_json"] else None,
            "error": json.loads(row["error_json"]) if row["error_json"] else None,
            "usage": json.loads(row["usage_json"]) if row["usage_json"] else {},
            "last_event_id": 0,
        }


def list_recent_runs(limit: int = 20) -> List[dict]:
    with _DB_LOCK, _conn() as conn:
        rows = conn.execute(
            "SELECT run_id, status, created, inputs_json FROM runs ORDER BY created DESC LIMIT ?", (limit,)
        ).fetchall()
        return [
            {
                "run_id": r["run_id"],
                "status": r["status"],
                "created": r["created"],
                "inputs": json.loads(r["inputs_json"]),
            }
            for r in rows
        ]


init_db()
