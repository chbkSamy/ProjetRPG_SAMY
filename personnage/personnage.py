from .interfaces import ClasseProvider
from .stats import Stats
class Personnage:
    def __init__(self, nom: str, classe: ClasseProvider):
        self.nom = nom
        self.classe = classe
        self.stats = classe.stats

    def afficher_recapitulatif(self) -> str:  
        return "\n".join([
            "\n=== Récapitulatif du personnage ===",
            f"Nom : {self.nom}",
            f"Classe : {self.classe.nom}",
            f"PV : {self.stats.pv}",
            f"PM : {self.stats.pm}",
            f"Force : {self.stats.force}",
            f"Intelligence : {self.stats.intelligence}",
            f"Defense : {self.stats.defense}",
            f"Résistance magique : {self.stats.resistance_magique}",
            f"Agilité : {self.stats.agilite}",
            f"Chance : {self.stats.chance}",
            f"Endurance : {self.stats.endurance}",
            f"Esprit : {self.stats.esprit}\n"
        ])
