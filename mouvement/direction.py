from enum import Enum

class Direction(Enum):
    NORD = 'N'
    EST = 'E'
    SUD = 'S'
    OUEST = 'O'

    @classmethod
    def get_order(cls):
        return [cls.NORD, cls.EST, cls.SUD, cls.OUEST]

    def gauche(self):
        return self._tourner(-1)

    def droite(self):
        return self._tourner(1)

    def _tourner(self, increment):
        order = self.get_order()
        return order[(order.index(self) + increment) % 4]
