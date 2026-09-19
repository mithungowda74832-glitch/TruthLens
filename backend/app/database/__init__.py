"""Database package initialization."""
from .db import (
    init_db,
    save_verification_record,
    get_recent_history,
    get_record_by_id,
    clear_all_history
)

__all__ = [
    "init_db",
    "save_verification_record",
    "get_recent_history",
    "get_record_by_id",
    "clear_all_history"
]
