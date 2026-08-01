from typing import List, Optional
from app.schemas.task import TaskCreate, TaskUpdate

# In-memory database
db_tasks = [
  { "id": 1, "title": "Task 1", "done": False },
  { "id": 2, "title": "Task 2", "done": False },
  { "id": 3, "title": "Task 3", "done": True },
];

class CRUDTask:
    def get_all(self) -> List[dict]:
        return db_tasks

    def get_by_id(self, task_id: int) -> Optional[dict]:
        for task in db_tasks:
            if task["id"] == task_id:
                return task
        return None

    def get_by_title(self, title: str) -> Optional[dict]:
        for task in db_tasks:
            if task["title"].lower() == title.lower():
                return task
        return None

    def create(self, obj_in: TaskCreate) -> dict:
        new_task = {
            "id": len(db_tasks) + 1,
            "title": obj_in.title.strip(),
            "done": obj_in.done,
        }
        db_tasks.append(new_task)
        return new_task

    def update(self, task_id: int, obj_in: TaskUpdate) -> Optional[dict]:
        task = self.get_by_id(task_id)
        if not task:
            return None

        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if field == "title" and value is not None:
                task[field] = value.strip()
            elif value is not None:
                task[field] = value

        return task

    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if not task:
            return False
        db_tasks.remove(task)
        return True

crud_task = CRUDTask()