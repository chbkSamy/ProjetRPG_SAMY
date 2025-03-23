from enum import Enum
from .stats import Stats
from .interfaces import MonstreProvider

class Monstres(Enum):
    SLIME = {
        "nom": "Slime",
        "stats": Stats(50,100,5,5,5,5,5,5,5,5)
    }
    SQUELETTE = {
        "nom": "Squelette",
        "stats": Stats(100,200,10,10,10,10,10,10,10,10)
    }
    DRAGON = {
        "nom": "Dragon",
        "stats": Stats(150,300,15,15,15,15,15,15,15,15)
    }

    @property
    def nom(self):
        return self.value["nom"]

    @property
    def stats(self):
        return self.value["stats"]


MonstreProvider.register(Monstres)
