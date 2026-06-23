from fastapi import APIRouter

router = APIRouter(
    prefix="/crowd",
    tags=["Crowd"]
)

@router.get("/")
def get_crowd():

    return {
        "route": "Koyambedu -> Airport",
        "crowd_level": "MEDIUM",
        "occupancy_percent": 65
    }