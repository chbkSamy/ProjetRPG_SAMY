from typing import Tuple
from .direction import Direction
from .moovementStrategies import STRATEGIES
from .interface import MovementStrategy

class CharacterMover:
    def __init__(self, position: Tuple[int, int], direction: Direction):
        self.position = position
        self.direction = direction

    def get_movement_strategy(self) -> MovementStrategy:
        return STRATEGIES[self.direction]

    def calculate_new_position(self) -> Tuple[int, int]:
        strategy = self.get_movement_strategy()
        dx, dy = strategy.get_vector()
        return (self.position[0] + dx, self.position[1] + dy)

    def rotate(self, rotation_type: str):
        if rotation_type == 'G':
            self.direction = self.direction.gauche()
        elif rotation_type == 'D':
            self.direction = self.direction.droite()
