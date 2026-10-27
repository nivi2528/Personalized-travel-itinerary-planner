from fastapi import APIRouter

from app.schemas.preference import PreferenceCreate

router = APIRouter(prefix="/preferences", tags=["preferences"])


@router.post("/")
def save_preferences(payload: PreferenceCreate):
    return {
        "saved": False,
        "message": "Database is not connected yet",
        "received": payload.model_dump(),
    }
