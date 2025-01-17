from dataclasses import dataclass

@dataclass
class PeopleDistribution:
    #todofix descr
    """
    dict = {"x-y": int} 
    where x - start age and y - end age
    for e.x. {"5-10": 532}
    """
    
    count : dict[str, int] = None

    def __post_init__(self):
        self.count = {**self._create_age_ranges(0,70,1), **self._create_age_ranges(70,100,5)}

    def _create_age_ranges(self, min_age: int, max_age: int, step: int) -> dict[str, int]:
        """Creates a dictionary of age ranges and 0 amount of people"""
        age_ranges: dict[str, int] = {}
        for x in range(min_age, max_age, step):
            y = x + step - 1
            age_ranges[f"{x}-{y}"] = 0
        return age_ranges
