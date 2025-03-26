from .interfaces import Positionnable

class Joueur(Positionnable):
    def __init__(self):
        self._position = (0, 0)
        self._orientation = 'N'
        self._directions = ['N', 'E', 'S', 'O']
        self.inventaire = []

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    @property
    def orientation(self) -> str:
        return self._orientation

    def set_orientation(self, direction: str) -> None:
        """Définit l’orientation à partir d'une commande ('N', 'S', 'E', 'O')."""
        if direction in self._directions:
            self._orientation = direction

    def tourner(self, sens: str) -> None:
        """Tourne le joueur à gauche ('G') ou à droite ('D')."""
        idx = self._directions.index(self._orientation)
        if sens == 'G':
            self._orientation = self._directions[(idx - 1) % 4]
        elif sens == 'D':
            self._orientation = self._directions[(idx + 1) % 4]

    def deplacer(self, x: int, y: int) -> None:
        self._position = (x, y)

    def get_orientation_vecteur(self) -> tuple[int, int]:
        """
        Retourne le vecteur de déplacement correspondant à l'orientation.
        "N" : avance vers le nord (augmentation de y),
        "S" : vers le sud (diminution de y),
        "E" : vers l'est (augmentation de x),
        "O" : vers l'ouest (diminution de x).
        """
        return {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'O': (-1, 0)
        }[self._orientation]
