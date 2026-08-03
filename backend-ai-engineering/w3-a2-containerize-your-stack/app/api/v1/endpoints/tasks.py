from typing import List
from fastapi import APIRouter, HTTPException, status
from app.crud.crud_task import task_crud
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter()

@router.get("/", response_model=List[TaskResponse])
def read_tasks():
    return task_crud.get_all()

@router.get("/{id}", response_model=TaskResponse)
def read_task(id: int):
    task = task_crud.get_by_id(id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "Task not found"}
        )
    return task

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    # Check for duplicate title if required by your domain logic
    existing_task = task_crud.get_by_title(payload.title)
    if existing_task:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": "Task with this title already exists"}
        )
    return task_crud.create(title=payload.title, done=payload.done)

@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, payload: TaskUpdate):
    # Check if task exists
    existing_task = task_crud.get_by_id(id)
    if not existing_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "Task not found"}
        )

    # Perform update with provided fields
    update_data = payload.model_dump(exclude_unset=True)
    updated_task = task_crud.update(id, update_data)
    return updated_task

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    success = task_crud.delete(id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "Task not found"}
        )
    return None