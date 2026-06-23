from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.db.models import Stop

router = APIRouter(
    prefix="/stops",
    tags=["Stops"]
)

@router.get("/")
def get_stops(
    db: Session = Depends(get_db)
):
    return db.query(Stop).all()

@router.get("/search")
def search_stops(
    q: str,
    db: Session = Depends(get_db)
):
    return db.query(Stop).filter(
        Stop.name.ilike(f"%{q}%")
    ).all()