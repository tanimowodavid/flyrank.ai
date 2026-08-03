from app.db.database import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table if it doesn't exist (PostgreSQL syntax)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        );
    """)

    # Check if table is empty
    cursor.execute("SELECT COUNT(*) AS count FROM tasks;")
    row = cursor.fetchone()
    # Support both dict-like and sequence results from different DB adapters
    if isinstance(row, dict):
        count = row.get("count", 0)
    else:
        # row can be a tuple/list (e.g., (count,))
        count = row[0] if row is not None else 0

    # Seed 3 example tasks ONLY if empty
    if count == 0:
        example_tasks = [
            ("Learn PostgreSQL with FastAPI", True),
            ("Build Stage 0 database layer", False),
            ("Submit FlyRank Assignment 2", False),
        ]
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (%s, %s);",
            example_tasks
        )
        conn.commit()
        print("Database initialized with 3 example tasks.")
    else:
        print("Database already contains tasks. Skipping seed.")

    cursor.close()
    conn.close()