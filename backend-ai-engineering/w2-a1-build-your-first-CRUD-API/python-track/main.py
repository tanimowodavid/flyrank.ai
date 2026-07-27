from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

tasks = [
  { "id": 1, "title": "Task 1", "done": False },
  { "id": 2, "title": "Task 2", "done": False },
  { "id": 3, "title": "Task 3", "done": True },
];

class Task(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# GET root
@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

# GET all tasks
@app.get("/task")
async def get_task():
    return { "tasks": tasks }

# GET task by ID
@app.get("/task/{id}")
async def get_task_by_id(id: int):
    task = [task for task in tasks if task["id"] == id]
    if len(task) == 0:
        raise HTTPException(
            status_code=404, 
            detail=f"Task with id {id} not found"
        )
    return { "tasks": task }

# create new task
@app.post("/task", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):

    # Validate non-empty name (stripping whitespace)
    if not task.title or task.title.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Title is required and cannot be empty"
        )
    
    # Auto-generate the next ID (highest ID + 1, or 1 if empty)
    next_id = max((t["id"] for t in tasks), default=0) + 1
    
    # Create the complete task dictionary
    new_task = {
        "id": next_id,
        "title": task.title.strip(),
        "done": False
    }
    
    tasks.append(new_task)
    return new_task
# =======================================
@app.put("/tasks/{id}")
async def update_task(id: int, task_data: TaskUpdate):
    # Find the task in memory
    task = next((t for t in tasks if t["id"] == id), None)
    
    # Return 404 if not found
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {id} not found"
        )

    # Exclude fields that weren't explicitly sent by the client
    # exclude_unset=True ignores default None values
    update_data = task_data.model_dump(exclude_unset=True)

    # 4. Reject empty updates (400 Bad Request)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Request body cannot be empty"
        )

    # Validate title if provided
    if "title" in update_data:
        title = update_data["title"]
        if not title or title.strip() == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title cannot be empty"
            )
        task["title"] = title.strip()

    # Update done status if provided
    if "done" in update_data:
        task["done"] = update_data["done"]

    return task

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int):
    # Find the task in memory
    task = next((t for t in tasks if t["id"] == id), None)
    
    # Return 404 if not found
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {id} not found"
        )
    tasks.remove(task)
    return 

# health check
@app.get("/health")
async def health():
    return { "status": "ok" }
