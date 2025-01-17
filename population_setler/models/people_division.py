from dataclasses import dataclass, field
from .people_distribution import PeopleDistribution

@dataclass(frozen=True)
class PeopleDivision:
    """todo"""

    men : PeopleDistribution = field(default_factory=PeopleDistribution)
    women : PeopleDistribution = field(default_factory=PeopleDistribution)
