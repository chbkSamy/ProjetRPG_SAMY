from enum import Enum
from .interfaces import Stats

class Monstres(Enum):
    SLIME = {
        "nom": "Slime",
        "stats": Stats(
            pv=50,
            pm=100,
            force=5,
            intelligence=5,
            defense=5,
            resistance_magique=5,
            agilite=5,
            chance=5,
            endurance=5,
            esprit=5
        )
    }

    DRAGON = {
        "nom": "Squelette",
        "stats": Stats(
            pv=100,
            pm=200,
            force=10,
            intelligence=10,
            defense=10,
            resistance_magique=10,
            agilite=10,
            chance=10,
            endurance=10,
            esprit=10
        )
    }

    @property
    def nom(self):
        return self.value["nom"]

    @property
    def stats(self):
        return self.value["stats"]
