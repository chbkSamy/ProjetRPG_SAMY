from enum import Enum
from .stats import Stats


class Classes(Enum):
    GUERRIER = {
        "nom": "Guerrier",
        "stats": Stats(
            pv=150, pm=150, force=15, intelligence=5,
            defense=12, resistance_magique=6, agilite=8,
            chance=5, endurance=10, esprit=4
        )
    }
    MAGE = {
        "nom": "Mage",
        "stats": Stats(
            pv=90, pm=150, force=4, intelligence=15,
            defense=5, resistance_magique=12, agilite=7,
            chance=6, endurance=5, esprit=10
        )
    }
    VOLEUR = {
        "nom": "Voleur",
        "stats": Stats(
            pv=110, pm=70, force=10, intelligence=7,
            defense=8, resistance_magique=7, agilite=15,
            chance=12, endurance=7, esprit=6
        )
    }

    @property
    def nom(self):
        return self.value["nom"]

    @property
    def stats(self):
        return self.value["stats"]
