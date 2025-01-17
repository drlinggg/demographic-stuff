from population_setler.models import Territory
from .balance_result_types import BalanceResult, UnknowFailure

class Balancer:
    #todo desc

    def balance_territories(self, territory: Territory) -> BalanceResult:
        #todo desc

        check_result: int = self._check_population_difference(territory)
        if check_result != 0:
            #todo компенсация если разница существует посчитать площади 
            #докинуть во внутренние территории или корневую idk в зависимости от доли ливинг ареа
            pass
        
        return UnknowFailure()

    def balance_houses(self, territory: Territory) -> BalanceResult:
        #todo desc
        if len(territory.houses) == 0:
            return NoHomesToBalance()

        return UnknowFailure()

    def _check_population_difference(self, territory: Territory) -> int:
        """
        Checks the difference between top territory
        and inner territories population 
        """
        difference: int = territory.get_self_population() - territory.get_total_population()
        return difference
