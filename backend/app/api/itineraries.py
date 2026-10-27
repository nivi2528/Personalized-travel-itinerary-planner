from fastapi import APIRouter

from app.schemas.itinerary import ItineraryGenerateRequest
from app.services.itinerary_generator import generate_placeholder_itinerary

router = APIRouter(prefix="/itineraries", tags=["itineraries"])


@router.post("/generate")
def generate_itinerary(payload: ItineraryGenerateRequest):
    return generate_placeholder_itinerary(payload)


@router.get("/")
def list_itineraries():
    return {"items": [], "message": "Saved itineraries will come from Supabase later"}


@router.put("/{itinerary_id}")
def edit_itinerary(itinerary_id: str):
    return {"id": itinerary_id, "updated": False, "message": "Edit is not implemented yet"}


@router.post("/{itinerary_id}/regenerate")
def regenerate_itinerary(itinerary_id: str):
    return {
        "id": itinerary_id,
        "regenerated": False,
        "message": "Regenerate is not implemented yet",
    }
