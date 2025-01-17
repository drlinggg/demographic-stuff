from dataclasses import dataclass

@dataclass
class House:
    """todo descr"""
    id : int | None = None
    population: int | None = None
    living_area: float | None = None

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError(
                       f"Id {self.id} of the house cannot be negative"
                    )
