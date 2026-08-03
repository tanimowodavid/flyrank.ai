from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs when app starts
    init_db()
    yield
    # Runs when app shuts down

app = FastAPI(
    title="Task Management API",
    description="Layered FastAPI Application with SQLite",
    version="2.0.0",
    lifespan=lifespan,
)

# Include aggregate router with /api/v1 prefix
app.include_router(api_router, prefix="/api/v1")
