from .interfaces import ClasseProvider
from .recapGenerator import PersonnageRecapGenerator

class Personnage:
    def __init__(self, nom: str, classe: ClasseProvider):
        self.nom = nom
        self.classe = classe
        self.stats = classe.stats

    def get_recap_data(self) -> tuple:
        """Fournit les données brutes pour le récapitulatif"""
        return (self.nom, self.classe.nom, self.stats)
