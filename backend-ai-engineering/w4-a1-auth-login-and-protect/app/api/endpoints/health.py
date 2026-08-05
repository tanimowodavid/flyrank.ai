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

