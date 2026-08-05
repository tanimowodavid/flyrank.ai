from fastapi import APIRouter
from app.api.endpoints import users, health

api_router = APIRouter()

# Mount feature endpoints
api_router.include_router(health.router, prefix="", tags=["System"])
api_router.include_router(users.router, prefix="", tags=["Auth"])