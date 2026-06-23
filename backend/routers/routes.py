from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.db.models import Route

router = APIRouter(
    prefix="/routes",
    tags=["Routes"]
)

@router.get("/")
def get_routes(
    db: Session = Depends(get_db)
):
    return db.query(Route).all()