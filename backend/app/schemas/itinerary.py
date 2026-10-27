from typing import List, Optional

from pydantic import BaseModel

from app.schemas.preference import PreferenceCreate


class DayPlan(BaseModel):
    day: int
    summary: str
    attractions: List[str] = []
    restaurants: List[str] = []
    accommodation: Optional[str] = None
    transportation: Optional[str] = None


class ItineraryGenerateRequest(BaseModel):
    preferences: PreferenceCreate
