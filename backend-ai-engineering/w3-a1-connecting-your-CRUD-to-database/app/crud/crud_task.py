from typing import List, Optional
from app.db.database import get_db_connection



class CRUDTask:
    def get_all(self) -> List[dict]:
        """Fetch all tasks from the SQLite database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, title, done FROM tasks")
        rows = cursor.fetchall()
        conn.close()
        
        # Convert sqlite3.Row objects to standard dictionaries (converting 0/1 to boolean)
        return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]

    def get_by_id(self, task_id: int) -> Optional[dict]:
        """Fetch a single task by ID from the SQLite database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row is None:
            return None
            
        return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}


    def get_by_title(self, title: str) -> Optional[dict]:
        """Fetch a task by title (case-insensitive) to check for duplicate titles."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, done FROM tasks WHERE LOWER(title) = LOWER(?)", (title.strip(),))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            return None
        return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}

    def create(self, title: str, done: bool = False) -> dict:
        """Insert a new task into SQLite database and return created task."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (title.strip(), 1 if done else 0)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return {"id": new_id, "title": title.strip(), "done": done}

    def update(self, task_id: int, updates: dict) -> Optional[dict]:
        """Update an existing task in the database."""
        current_task = self.get_by_id(task_id)
        if not current_task:
            return None

        # Determine final values after applying updates
        new_title = updates.get("title", current_task["title"])
        if isinstance(new_title, str):
            new_title = new_title.strip()
            
        new_done = updates.get("done", current_task["done"])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
            (new_title, 1 if new_done else 0, task_id)
        )
        conn.commit()
        conn.close()

        return {"id": task_id, "title": new_title, "done": new_done}

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        return rows_affected > 0



task_crud = CRUDTask()