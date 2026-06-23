from fastapi import APIRouter

from backend.models.journey_schema import JourneyRequest

from backend.engines.fare_calculator import FareCalculator
from backend.engines.crowd_predictor import CrowdPredictor
from backend.engines.risk_engine import RiskEngine
from backend.engines.stress_calculator import StressCalculator
from backend.engines.confidence_scorer import ConfidenceScorer
from backend.engines.smart_route_advisor import SmartRouteAdvisor
from backend.engines.xai_explainer import XAIExplainer

from backend.models.route_metrics import RouteMetrics

from sqlalchemy.orm import Session
from fastapi import Depends
from backend.dependencies import get_db

from backend.db.models import Journey


router = APIRouter(
    prefix="/journey",
    tags=["Journey"]
)


@router.post("/plan")
def plan_journey(request: JourneyRequest,
    db: Session = Depends(get_db)):

    fare = FareCalculator().calculate(
        distance_km=12
    )

    crowd = CrowdPredictor().predict(
        crowd_score=0.55
    )

    risk = RiskEngine().evaluate(
        accident_probability=0.20,
        weather_risk=0.10,
        crime_risk=0.30
    )

    stress = StressCalculator().calculate(
        crowd_score=crowd.crowd_score,
        risk_score=risk.risk_score,
        travel_time=30
    )

    confidence = ConfidenceScorer().calculate(
        crowd_confidence=crowd.confidence
    )

    route = RouteMetrics(
        route_id="Metro-001",
        total_time=30,
        total_cost=fare,
        crowd_score=crowd.crowd_score,
        crowd_level=crowd.crowd_level,
        risk_score=risk.risk_score,
        risk_level=risk.risk_level,
        stress_score=stress,
        confidence_score=confidence
    )

    best_route = SmartRouteAdvisor().recommend(
        [route]
    )

    
    explanation = XAIExplainer().explain(
        best_route
    )

    new_journey = Journey(
    source=request.source,
    destination=request.destination,
    selected_route=best_route.route_id,
    fare=best_route.total_cost,
    travel_time=best_route.total_time)
    db.add(new_journey)
    db.commit()


    return {
        "source": request.source,
        "destination": request.destination,
        "route_id": best_route.route_id,
        "fare": best_route.total_cost,
        "travel_time": best_route.total_time,
        "crowd_level": best_route.crowd_level,
        "risk_level": best_route.risk_level,
        "stress_score": best_route.stress_score,
        "confidence_score": best_route.confidence_score,
        "explanation": explanation
    }

@router.get("/history")
def get_journey_history(db: Session = Depends(get_db)):
    return db.query(Journey).all()
