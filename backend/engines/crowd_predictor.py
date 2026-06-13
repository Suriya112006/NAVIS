from models.crowd_model import CrowdData


class CrowdPredictor:

    def predict(self, crowd_score: float) -> CrowdData:

        if crowd_score >= 0.75:
            level = "High"
            confidence = 0.92

        elif crowd_score >= 0.40:
            level = "Medium"
            confidence = 0.87

        else:
            level = "Low"
            confidence = 0.95

        return CrowdData(
            crowd_level=level,
            crowd_score=crowd_score,
            confidence=confidence
        )