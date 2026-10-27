from app.schemas.itinerary import ItineraryGenerateRequest


def generate_placeholder_itinerary(payload: ItineraryGenerateRequest) -> dict:
    destination = payload.preferences.destination
    return {
        "generated": False,
        "destination": destination,
        "days": [
            {
                "day": 1,
                "summary": f"Placeholder day in {destination}",
                "attractions": [],
                "restaurants": [],
                "accommodation": None,
                "transportation": None,
            }
        ],
        "message": "Real itineraries will use Google Cloud AI later",
    }
