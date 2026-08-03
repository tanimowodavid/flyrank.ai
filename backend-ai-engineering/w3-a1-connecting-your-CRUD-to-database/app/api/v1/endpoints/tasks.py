from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.crud.crud_task import crud_task

router = APIRouter()

@router.get("/", response_model=List[TaskResponse])
def get_tasks():
    return crud_task.get_all()

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = crud_task.get_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )
    return task

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    if crud_task.get_by_title(task_in.title):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="A task with this title already exists"
        )
    return crud_task.create(task_in)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_in: TaskUpdate):
    updated_task = crud_task.update(task_id, task_in)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )
    return updated_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    success = crud_task.delete(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with ID {task_id} not found"
        )