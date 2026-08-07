from fastapi import APIRouter
from app.api.endpoints import users, health, public, protected

api_router = APIRouter()

# Mount feature endpoints
api_router.include_router(health.router, prefix="", tags=["System"])
api_router.include_router(users.router, prefix="", tags=["Auth"])
api_router.include_router(public.router, prefix="", tags=["Public"])
api_router.include_router(protected.router, prefix="", tags=["Protected"])