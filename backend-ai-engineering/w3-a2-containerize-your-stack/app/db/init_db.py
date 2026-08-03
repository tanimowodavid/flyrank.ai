from app.db.database import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    # Check if table is empty
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    # Seed 3 example tasks ONLY if empty
    if count == 0:
        example_tasks = [
            ("Learn SQLite with FastAPI", 1),
            ("Build Stage 0 database layer", 0),
            ("Submit FlyRank Assignment 2", 0),
        ]
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            example_tasks
        )
        conn.commit()
        print("Database initialized with 3 example tasks.")
    else:
        print("Database already contains tasks. Skipping seed.")

    conn.close()

