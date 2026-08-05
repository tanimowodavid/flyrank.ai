from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.api.api import api_router
app = FastAPI(
    title="Task Management API",
    description="Layered FastAPI Application with SQLite",
    version="1.0.0",
)

# Include aggregate router with /api/v1 prefix
app.include_router(api_router, prefix="/api/v1")