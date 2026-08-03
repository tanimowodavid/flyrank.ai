from typing import List, Optional
from app.db.database import get_db_connection


class CRUDTask:
    def get_all(self) -> List[dict]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, done FROM tasks ORDER BY id ASC;")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_by_id(self, task_id: int) -> Optional[dict]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, done FROM tasks WHERE id = %s;", (task_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def get_by_title(self, title: str) -> Optional[dict]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, done FROM tasks WHERE LOWER(title) = LOWER(%s);", (title.strip(),))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def create(self, title: str, done: bool = False) -> dict:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id, title, done;",
            (title.strip(), done)
        )
        new_task = cursor.fetchone()
        conn.commit()
        conn.close()
        if new_task is None:
            raise RuntimeError("Failed to create task")
        return dict(new_task)

    def update(self, task_id: int, updates: dict) -> Optional[dict]:
        current_task = self.get_by_id(task_id)
        if not current_task:
            return None

        new_title = updates.get("title", current_task["title"])
        new_done = updates.get("done", current_task["done"])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET title = %s, done = %s WHERE id = %s RETURNING id, title, done;",
            (new_title, new_done, task_id)
        )
        updated_task = cursor.fetchone()
        conn.commit()
        conn.close()
        if updated_task is None:
            return None
        return dict(updated_task)

    def delete(self, task_id: int) -> bool:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        return rows_affected > 0

task_crud = CRUDTask()