from enum import Enum
from .stats import Stats
from .interfaces import ClasseProvider

class Classes(Enum):
    GUERRIER = {
        "nom": "Guerrier",
        "stats": Stats(150, 150, 15, 5, 12, 6, 8, 5, 10, 4)
    }
    MAGE = {
        "nom": "Mage",
        "stats": Stats(90,150,4,15,5,12,7,6,5,10)
    }
    VOLEUR = {
        "nom": "Voleur",
        "stats": Stats(110,70,10,7,8,7,15,12,7,6)
    }

    @property
    def nom(self):
        return self.value["nom"]

    @property
    def stats(self):
        return self.value["stats"]


ClasseProvider.register(Classes)
