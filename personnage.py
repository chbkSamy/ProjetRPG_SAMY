from classes import Classes

class Personnage(Classes):
    def __init__(self, nom_personnage, classe):
        super().__init__(classe.nom, classe.pv, classe.pm, classe.force, classe.intelligence,
                         classe.defense, classe.resistance_magique, classe.agilite, classe.chance,
                         classe.endurance, classe.esprit)
        self.nom_personnage = nom_personnage
        self.classe = classe.nom


    @classmethod
    def initialiser_personnage(cls):
        nom = input("Entrez le nom du personnage : ")
        while len(nom) < 3 or len(nom) > 10:
            print("Le nom du personnage doit avoir entre 3 et 10 caractères.")
            nom = input("Entrez le nom du personnage : ")
        classes_disponibles = [
            Classes("Guerrier", 150, 150, 15, 5, 12, 6, 8, 5, 10, 4),
            Classes("Mage", 90, 150, 4, 15, 5, 12, 7, 6, 5, 10),
            Classes("Voleur", 110, 70, 10, 7, 8, 7, 15, 12, 7, 6)
        ]
        print("Choisissez une classe :")
        for i, classe in enumerate(classes_disponibles):
            print(f"{i + 1}. {classe.nom}")
        choix = int(input("Entrez le numéro de la classe choisie : "))
        selected_classe = classes_disponibles[choix - 1]
        return cls(nom, selected_classe)


    def recapitulatif_personnage(self):
        print("Recapitulatif du personnage :")
        print(f"Nom : {self.nom_personnage}")
        print(f"Classe : {self.classe}")
        print(f"PV : {self.pv}")
        print(f"PM : {self.pm}")
        print(f"Force : {self.force}")
        print(f"Intelligence : {self.intelligence}")
        print(f"Defense : {self.defense}")
        print(f"Resistance magique : {self.resistance_magique}")
        print(f"Agilité : {self.agilite}")
        print(f"Chance : {self.chance}")
        print(f"Endurance : {self.endurance}")
        print(f"Esprit : {self.esprit}")



