from abc import ABC, abstractmethod
from .direction import Direction

# Interface
class MovementStrategy(ABC):
    @abstractmethod
    def get_vector(self) -> tuple[int, int]:
        pass


