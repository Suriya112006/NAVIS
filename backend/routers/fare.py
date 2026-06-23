from fastapi import APIRouter

router = APIRouter(
    prefix="/fare",
    tags=["Fare"]
)

@router.get("/")
def get_fare():
    return {
        "route": "Koyambedu -> Airport",
        "fare": 45
    }