from fastapi import APIRouter
import time

router = APIRouter()
start_time = time.time()

@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "uptime_seconds": round(time.time() - start_time, 2),
    }

@router.get("/")
def api_meta():
    return {
        "name": "Task Management API",
        "version": "1.0.0",
        "docs": "/docs"
    }