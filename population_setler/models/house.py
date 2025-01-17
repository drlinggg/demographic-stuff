from dataclasses import dataclass

@dataclass
class House:
    """todo descr"""
    id : int | None = None
    population: int | None = None
    living_area: float | None = None
