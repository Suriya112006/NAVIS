from pydantic import BaseModel

class StopResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    stop_type: str

    class Config:
        from_attributes = True