from .personnage import Personnage
from .classes import Classes

class PersonnageFactory:
    @staticmethod
    def initialiser_personnage() -> Personnage:
        nom = input("Nom du personnage : ")
        while len(nom) < 3 or len(nom) > 10:
            nom = input("Nom invalide (3-10 caractères) : ")

        print("Classes disponibles :")
        for idx, classe in enumerate(Classes):
            print(f"{idx + 1}. {classe.nom}")

        choix = int(input("Choix : ")) - 1
        return Personnage(nom, list(Classes)[choix])
