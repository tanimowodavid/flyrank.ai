from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="Task Management API",
    description="Production-ready Layered FastAPI Application",
    version="1.0.0"
)

# Include aggregate router with /api/v1 prefix
app.include_router(api_router, prefix="/api/v1")