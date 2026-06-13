from models.route_metrics import RouteMetrics


class SmartRouteAdvisor:
    """
    Chooses the best route.
    """

    def recommend(self, routes: list[RouteMetrics]) -> RouteMetrics:

        if not routes:
            raise ValueError("No routes available")

        return min(
            routes,
            key=lambda r: (
                r.risk_score,
                r.stress_score,
                r.total_time
            )
        )