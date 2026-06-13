from models.route_metrics import RouteMetrics


class XAIExplainer:
    """
    Generates human-readable route explanations.
    """

    def explain(self, route: RouteMetrics) -> str:

        return (
            f"Route {route.route_id} selected because "
            f"crowd level is {route.crowd_level}, "
            f"risk level is {route.risk_level}, "
            f"estimated cost is ₹{route.total_cost}, "
            f"travel time is {route.total_time} minutes, "
            f"and confidence score is {route.confidence_score:.2f}."
        )