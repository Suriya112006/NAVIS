from dataclasses import dataclass
from typing import List


@dataclass
class RiskData:

    risk_level: str

    risk_score: float

    factors: List[str]