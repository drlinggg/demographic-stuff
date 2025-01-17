from dataclasses import dataclass, field
from .house import House
from .people_division import PeopleDivision

@dataclass
class Territory:
#todo descr
    name: str
    population: PeopleDivision | int | None = None
    inner_territories: list["Territory"] = field(default_factory=list["Territory"])
    houses: list["House"] = field(default_factory=list["House"])

