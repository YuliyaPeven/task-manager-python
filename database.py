import sqlite3

DB_NAME = "tasks.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                status TEXT DEFAULT 'todo',
                deadline TEXT
            )
        """)
