from .interfaces import ClasseProvider
from .stats import Stats

class Personnage:
    def __init__(self, nom: str, classe: ClasseProvider):
        self.nom = nom
        self.classe = classe
        self.stats = classe.stats

    def recapitulatif_personnage(self):
        print("\n=== Récapitulatif du personnage ===")
        print(f"Nom : {self.nom}")
        print(f"Classe : {self.classe.nom}")
        print(f"PV : {self.stats.pv}")
        print(f"PM : {self.stats.pm}")
        print(f"Force : {self.stats.force}")
        print(f"Intelligence : {self.stats.intelligence}")
        print(f"Defense : {self.stats.defense}")
        print(f"Résistance magique : {self.stats.resistance_magique}")
        print(f"Agilité : {self.stats.agilite}")
        print(f"Chance : {self.stats.chance}")
        print(f"Endurance : {self.stats.endurance}")
        print(f"Esprit : {self.stats.esprit}\n")
