from dataclasses import dataclass
from typing import Optional


@dataclass
class RouteMetrics:

    route_id: str

    total_time: float
    total_cost: float

    crowd_score: float = 0.0
    risk_score: float = 0.0
    stress_score: float = 0.0
    confidence_score: float = 0.0

    crowd_level: Optional[str] = None
    risk_level: Optional[str] = None

    final_score: float = 0.0