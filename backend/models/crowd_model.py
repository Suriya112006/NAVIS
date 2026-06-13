from dataclasses import dataclass


@dataclass
class CrowdData:

    crowd_level: str

    crowd_score: float

    confidence: float