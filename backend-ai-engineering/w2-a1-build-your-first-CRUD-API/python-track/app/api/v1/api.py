from fastapi import APIRouter
from app.api.v1.endpoints import tasks, health

api_router = APIRouter()

# Mount feature endpoints
api_router.include_router(health.router, prefix="", tags=["System"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])