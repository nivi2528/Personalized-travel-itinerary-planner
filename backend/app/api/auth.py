from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/status")
def auth_status():
    return {"connected": False, "message": "Supabase auth is not set up yet"}
