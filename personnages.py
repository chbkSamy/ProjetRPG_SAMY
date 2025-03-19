from classes.classe import Classe
from classes.guerrier import Guerrier
from classes.mage import Mage
from classes.voleur import Voleur


class Personnage (Classe):
    def __init__(self, nom_perso, classe_perso):
        super().__init__(classe_perso.nom, classe_perso.pv, classe_perso.pm, classe_perso.force,
                         classe_perso.intelligence, classe_perso.défense, 
                         classe_perso.résistance_magique, classe_perso.agilité, 
                         classe_perso.chance, classe_perso.endurance, classe_perso.esprit)
        self.nom_personnage = nom_perso
        self.classe = classe_perso
    
    def attaquer(self):
        return self.force
        
    def nom_personnage():
        nom_perso = input("Entrez le nom de votre personnage: ")
        while len(nom_perso) < 2 or len(nom_perso) > 15:
            print("Le nom de votre personnage doit être compris entre 2 et 15 caractères")
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