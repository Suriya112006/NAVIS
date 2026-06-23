from fastapi import APIRouter

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)

@router.get("/")
def get_risk():

    return {
        "route": "Koyambedu -> Airport",
        "risk_level": "LOW",
        "risk_score": 12
    }