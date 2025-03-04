from classes.guerrier import Guerrier
from classes.mage import Mage
from classes.voleur import Voleur


class Personnage:
    def __init__(self, nom_perso, classe_perso):
        self.nom_personnage = nom_perso
        self.classe = classe_perso


    def nom_personnage():
        nom_perso = input("Entrez le nom de votre personnage: ")
        while len(nom_perso) < 2 or len(nom_perso) > 15:
            print("Le nom de votre personnage doit être compris entre 3 et 15 caractères")
            nom_perso = input("Entrez le nom de votre personnage: ")
        return nom_perso



    def choix_classe():
        classe_dispo = [Guerrier(), Mage(), Voleur()]
        print("Choisissez votre classe:")
        for i, classe in enumerate(classe_dispo):
            print(f"{i+1}. {classe.nom}")
        choix = int(input("Entrez le numéro de la classe choisie: "))
        return classe_dispo[choix-1]

    def recap_perso(self):
        print(f"Nom: {self.nom_personnage}")
        print(f"Classe: {self.classe.nom}")
        print(f"PV: {self.classe.pv}")
        print(f"PM: {self.classe.pm}")
        print(f"Force: {self.classe.force}")
        print(f"Intelligence: {self.classe.intelligence}")
        print(f"Défense: {self.classe.défense}")
        print(f"Résistance magique: {self.classe.résistance_magique}")
        print(f"Agilité: {self.classe.agilité}")
        print(f"Chance: {self.classe.chance}")
        print(f"Endurance: {self.classe.endurance}")
        print(f"Esprit: {self.classe.esprit}")
        print("Personnage créé avec succès !") 