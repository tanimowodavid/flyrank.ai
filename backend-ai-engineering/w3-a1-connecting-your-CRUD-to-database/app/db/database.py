import sqlite3
from pathlib import Path

# DB file will be stored in the root directory
DB_PATH = Path(__file__).resolve().parent.parent.parent / "tasks.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Access columns by name: row["title"]
    return conn

