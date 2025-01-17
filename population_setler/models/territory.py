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

    def get_living_area(self) -> float:
        """Get total living area of all houses of the territory (its inner territories)."""
        if len(self.inner_territories) != 0:
            return sum(it.get_total_living_area() for it in self.inner_territories)
        return sum(house.living_area if house.living_area is not None else 0.0 for house in self.houses)

    def get_population(self) -> int:
        if len(self.inner_territories) != 0:
            return sum(it.get_population for it in self.inner_territories)
        return self.population.total()

    def get_houses(self) -> list["house"]:
        houses = list["house"]
        if len(self.inner_territories) != 0:
            return [house for it in self.inner_territories for house in it.get_houses()]
        return self.houses

    def get_houses_population(self) -> int:
        pass
