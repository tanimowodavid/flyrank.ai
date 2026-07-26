from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
  { "id": 1, "name": "Task 1", "done": False },
  { "id": 2, "name": "Task 2", "done": False },
  { "id": 3, "name": "Task 3", "done": True },
];

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
    return { "tasks": [task for task in tasks if task["id"] == id] }

# health check
@app.get("/health")
async def health():
    return { "status": "ok" }
