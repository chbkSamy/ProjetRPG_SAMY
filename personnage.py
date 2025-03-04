from classes import Classes
from stats import Stats

class Personnage:
    STATS_PAR_CLASSE = {
        Classes.GUERRIER: Stats(
            pv=150, pm=150, force=15, intelligence=5,
            defense=12, resistance_magique=6, agilite=8,
            chance=5, endurance=10, esprit=4
        ),
        Classes.MAGE: Stats(
            pv=90, pm=150, force=4, intelligence=15,
            defense=5, resistance_magique=12, agilite=7,
            chance=6, endurance=5, esprit=10
        ),
        Classes.VOLEUR: Stats(
            pv=110, pm=70, force=10, intelligence=7,
            defense=8, resistance_magique=7, agilite=15,
            chance=12, endurance=7, esprit=6
        )
    }

    def __init__(self, nom: str, classe: Classes):
        self.nom = nom
        self.classe = classe
        self.stats = self.STATS_PAR_CLASSE[classe]

    @classmethod
    def initialiser_personnage(cls):
        nom = input("Nom du personnage : ")
        while len(nom) < 3 or len(nom) > 10:
            nom = input("Nom invalide (3-10 caractères) : ")

        print("Classes disponibles :")
        for idx, classe in enumerate(Classes):
            print(f"{idx + 1}. {classe.value}")

        choix = int(input("Choix : ")) - 1
        return cls(nom, list(Classes)[choix])

    def recapitulatif_personnage(self):
        print("\n=== Récapitulatif du personnage ===")
        print(f"Nom : {self.nom}")
        print(f"Classe : {self.classe.value}")
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



