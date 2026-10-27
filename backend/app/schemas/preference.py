from typing import List, Optional

from pydantic import BaseModel


class PreferenceCreate(BaseModel):
    destination: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    budget: Optional[str] = None
    travel_style: Optional[str] = None
    interests: List[str] = []
