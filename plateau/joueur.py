from mouvement.personnagemoove import CharacterMover
from mouvement.direction import Direction


class Joueur:
    def __init__(self):
        self.mover = CharacterMover((0, 0), Direction.NORD)
        self.inventaire = []

    def calculate_new_position(self) -> tuple[int, int]:
        return self.mover.calculate_new_position()

    def deplacer(self, new_position: tuple[int, int]):
        self.mover.position = new_position

    @property
    def position(self):
        return self.mover.position

    @property
    def direction(self):
        return self.mover.direction

    def tourner(self, commande: str):
        self.mover.rotate(commande)
