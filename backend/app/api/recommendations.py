from fastapi import APIRouter

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/")
def get_recommendations():
    return {
        "attractions": [],
        "restaurants": [],
        "accommodations": [],
        "transportation": [],
        "message": "Google Cloud AI recommendations are not connected yet",
    }
