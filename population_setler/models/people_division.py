from dataclasses import dataclass, field
from .people_distribution import PeopleDistribution

@dataclass(frozen=True)
class PeopleDivision:
    """todo"""

    men : PeopleDistribution = field(default_factory=PeopleDistribution)
    women : PeopleDistribution = field(default_factory=PeopleDistribution)

    def __post_init__(self):
        if len(self.men.count) != len(self.women.count):
            raise ValueError(
                    f"Length of men ({len(self.men)}) and women ({len(self.women)}) age ranges "
                    "must be the same"
                    )

    def total_amount(self) -> int:
        #todo desc
        men_amount: int = sum(age_range_amount for age_range_amount in self.men.count.values())
        women_amount: int = sum(age_range_amount for age_range_amount in self.women.count.values())
        return men_amount + women_amount

