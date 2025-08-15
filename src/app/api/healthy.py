from fastapi import APIRouter
from core.config import APP_NAME, VERSION

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "App Name": APP_NAME,
        "Version": VERSION,
        "status": "Healthy"
    }