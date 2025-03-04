from classes import Classes

class Personnage:
    def __init__(self, nom: str, classe: Classes):
        self.nom = nom
        self.classe = classe
        self.stats = classe.stats

    @classmethod
    def initialiser_personnage(cls):
        nom = input("Nom du personnage : ")
        while len(nom) < 3 or len(nom) > 10:
            nom = input("Nom invalide (3-10 caractères) : ")

        print("Classes disponibles :")
        for idx, classe in enumerate(Classes):
            print(f"{idx + 1}. {classe.nom}")

        choix = int(input("Choix : ")) - 1
        return cls(nom, list(Classes)[choix])

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
