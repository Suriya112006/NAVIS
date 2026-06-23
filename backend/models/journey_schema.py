from pydantic import BaseModel

class JourneyRequest(BaseModel):
    source: str
    destination: str
    preference: str