"""
TruthLens SQLite Database Layer.
Stores verification history, claim records, and source citations.
"""

import sqlite3
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

logger = logging.getLogger("truthlens.db")

DB_DIR = Path(__file__).resolve().parent.parent.parent
DB_FILE = DB_DIR / "truthlens_history.db"


def get_connection() -> sqlite3.Connection:
    """Returns a SQLite connection with row dict access."""
    conn = sqlite3.connect(str(DB_FILE))
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Initializes the database schema if tables do not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Claims history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS claims (
                id TEXT PRIMARY KEY,
                claim_text TEXT NOT NULL,
                verdict TEXT NOT NULL,
                confidence INTEGER NOT NULL,
                explanation TEXT NOT NULL,
                limitations TEXT,
                created_at TEXT NOT NULL,
                raw_response_json TEXT NOT NULL
            )
        """)
        
        # Sources table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sources (
                id TEXT PRIMARY KEY,
                claim_id TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                source_name TEXT NOT NULL,
                stance TEXT NOT NULL,
                snippet TEXT,
                FOREIGN KEY(claim_id) REFERENCES claims(id) ON DELETE CASCADE
            )
        """)
        conn.commit()
    logger.info(f"Database initialized at {DB_FILE}")


def save_verification_record(response_data: Dict[str, Any]) -> None:
    """Persists a full verification response into the SQLite database."""
    claim_id = response_data["id"]
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # Save claim
            cursor.execute("""
                INSERT OR REPLACE INTO claims (
                    id, claim_text, verdict, confidence, explanation, limitations, created_at, raw_response_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                claim_id,
                response_data["claim"],
                response_data["verdict"],
                response_data["confidence"],
                response_data["explanation"],
                response_data.get("limitations_and_uncertainty", ""),
                response_data["created_at"],
                json.dumps(response_data)
            ))
            
            # Save individual sources from both supporting and contradicting evidence
            for ev in response_data.get("supporting_evidence", []):
                cursor.execute("""
                    INSERT OR REPLACE INTO sources (
                        id, claim_id, title, url, source_name, stance, snippet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    ev.get("id"),
                    claim_id,
                    ev.get("title", ""),
                    ev.get("url", ""),
                    ev.get("source", ""),
                    "supporting",
                    ev.get("snippet", "")
                ))

            for ev in response_data.get("contradicting_evidence", []):
                cursor.execute("""
                    INSERT OR REPLACE INTO sources (
                        id, claim_id, title, url, source_name, stance, snippet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    ev.get("id"),
                    claim_id,
                    ev.get("title", ""),
                    ev.get("url", ""),
                    ev.get("source", ""),
                    "contradicting",
                    ev.get("snippet", "")
                ))

            conn.commit()
        logger.info(f"Saved verification record: {claim_id}")
    except Exception as e:
        logger.error(f"Failed to persist verification history: {e}", exc_info=True)


def get_recent_history(limit: int = 20) -> List[Dict[str, Any]]:
    """Fetches recent claims history for display in the UI drawer."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, claim_text, verdict, confidence, explanation, created_at
                FROM claims
                ORDER BY created_at DESC
                LIMIT ?
            """, (limit,))
            rows = cursor.fetchall()
            return [
                {
                    "id": row["id"],
                    "claim": row["claim_text"],
                    "verdict": row["verdict"],
                    "confidence": row["confidence"],
                    "explanation": row["explanation"],
                    "created_at": row["created_at"]
                }
                for row in rows
            ]
    except Exception as e:
        logger.error(f"Failed to query history: {e}")
        return []


def get_record_by_id(claim_id: str) -> Optional[Dict[str, Any]]:
    """Retrieves full serialized verification payload to reopen a past analysis."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT raw_response_json FROM claims WHERE id = ?", (claim_id,))
            row = cursor.fetchone()
            if row:
                return json.loads(row["raw_response_json"])
            return None
    except Exception as e:
        logger.error(f"Failed to fetch record {claim_id}: {e}")
        return None


def clear_all_history() -> bool:
    """Wipes claims and sources history tables."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sources")
            cursor.execute("DELETE FROM claims")
            conn.commit()
        return True
    except Exception as e:
        logger.error(f"Failed to clear history: {e}")
        return False
