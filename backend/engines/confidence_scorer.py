class ConfidenceScorer:
    """
    Computes overall confidence score.
    """

    def calculate(
        self,
        crowd_confidence: float,
        risk_confidence: float = 0.90
    ) -> float:

        confidence = (
            crowd_confidence * 0.5 +
            risk_confidence * 0.5
        )

        return round(confidence, 2)