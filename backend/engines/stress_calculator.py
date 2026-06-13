class StressCalculator:
    """
    Calculates travel stress score.
    """

    def calculate(
        self,
        crowd_score: float,
        risk_score: float,
        travel_time: float
    ) -> float:

        stress_score = (
            crowd_score * 0.4 +
            risk_score * 0.4 +
            min(travel_time / 120, 1.0) * 0.2
        )

        return round(stress_score, 2)