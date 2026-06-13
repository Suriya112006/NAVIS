class FareCalculator:
    """
    Calculates estimated route fare.
    """

    BASE_FARE = 20.0
    COST_PER_KM = 12.0

    def calculate(
        self,
        distance_km: float,
        surge_multiplier: float = 1.0
    ) -> float:

        fare = (
            self.BASE_FARE +
            (distance_km * self.COST_PER_KM)
        ) * surge_multiplier

        return round(fare, 2)