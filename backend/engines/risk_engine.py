from typing import List
from backend.models.risk_model import RiskData


class RiskEngine:
    """
    Route risk analysis engine.
    """

    def evaluate(
        self,
        accident_probability: float,
        weather_risk: float,
        crime_risk: float
    ) -> RiskData:

        risk_score = (
            accident_probability * 0.5 +
            weather_risk * 0.3 +
            crime_risk * 0.2
        )

        factors: List[str] = []

        if accident_probability > 0.6:
            factors.append("High accident probability")

        if weather_risk > 0.6:
            factors.append("Severe weather conditions")

        if crime_risk > 0.6:
            factors.append("Unsafe zone detected")

        if risk_score >= 0.75:
            risk_level = "High"

        elif risk_score >= 0.40:
            risk_level = "Medium"

        else:
            risk_level = "Low"

        return RiskData(
            risk_level=risk_level,
            risk_score=round(risk_score, 2),
            factors=factors
        )