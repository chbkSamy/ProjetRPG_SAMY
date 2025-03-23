from typing import Iterable
from .interfaces import ClasseProvider
from .personnage import Personnage

class PersonnageFactory:
    def __init__(self, classes_disponibles: Iterable[ClasseProvider]):
        self.classes_disponibles = list(classes_disponibles)

    def creer_personnage(self) -> Personnage:
        nom = input("Nom du personnage : ")
        while len(nom) < 3 or len(nom) > 10:
            nom = input("Nom invalide (3-10 caractères) : ")

        print("Classes disponibles :")
        for idx, classe in enumerate(self.classes_disponibles):
            print(f"{idx + 1}. {classe.nom}")

        choix = int(input("Choix : ")) - 1
        return Personnage(nom, self.classes_disponibles[choix])
