from .interface import MovementStrategy
from .direction import Direction
class NorthMovement(MovementStrategy):
    def get_vector(self) -> tuple[int, int]:
        return (0, -1)

class EastMovement(MovementStrategy):
    def get_vector(self) -> tuple[int, int]:
        return (1, 0)

class SouthMovement(MovementStrategy):
    def get_vector(self) -> tuple[int, int]:
        return (0, 1)

class WestMovement(MovementStrategy):
    def get_vector(self) -> tuple[int, int]:
        return (-1, 0)

STRATEGIES = {
    Direction.NORD: NorthMovement(),
    Direction.EST: EastMovement(),
    Direction.SUD: SouthMovement(),
    Direction.OUEST: WestMovement()
}
