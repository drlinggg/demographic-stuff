from dataclasses import dataclass
from abc import ABC, abstractmethod

class BalanceResult(ABC):
    #todo desc
    @abstractmethod
    def is_success(self) -> bool:
        pass

@dataclass(frozen=True)
class Success(BalanceResult):
    def is_success(self) -> bool:
        return True

@dataclass(frozen=True)
class UnknowFailure(BalanceResult):
    def is_success(self) -> bool:
        return False

@dataclass(frozen=True)
class NoHomesToBalance(BalanceResult):
    #todo desc
    def is_success(self) -> bool:
        return False 
