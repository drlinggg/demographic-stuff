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
        """Gets total living area of all houses of the territory (its inner territories)."""
        if len(self.inner_territories) != 0:
            return sum(it.get_total_living_area() for it in self.inner_territories)
        return sum(house.living_area if house.living_area is not None else 0.0 for house in self.houses)

    #todo fix naming
    def get_total_population(self) -> int:
        #todo desc
        if len(self.inner_territories) != 0:
            return sum(it.get_total_population for it in self.inner_territories)
        return self.get_self_population()

    def get_self_population(self) -> int:
        #todo desc
        #needs because not every territory has peopledivision
        if isinstance(self.population, PeopleDivision):
            return self.population.total_amount()
        else:
            return self.population


    def get_houses(self) -> list["house"]:
        #todo desc
        houses = list["house"]
        if len(self.inner_territories) != 0:
            return [house for it in self.inner_territories for house in it.get_houses()]
        return self.houses

    def get_houses_population(self) -> int:
        #todo
        pass
