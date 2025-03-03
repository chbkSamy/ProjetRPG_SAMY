from classes import Classe
from personnages import Personnage

guerrier = Classe("Guerrier", 150, 50, 15, 5, 12, 6, 8, 5, 10, 4)
mage = Classe("Mage", 90, 150, 4, 15, 5, 12, 7, 6, 5, 10)
voleur = Classe("Voleur", 110, 70, 10, 7, 8, 7, 15, 12, 7, 6)
classe_dispo = [guerrier, mage, voleur]

def nom_personnage():
    nom_perso = input("Entrez le nom de votre personnage: ")
    while len(nom_perso) < 2 or len(nom_perso) > 15:
        print("Le nom de votre personnage doit être compris entre 3 et 15 caractères")
        nom_perso = input("Entrez le nom de votre personnage: ")
    return nom_perso

def choix_classe():
    print("Choisissez votre classe:")
    for i, classe in enumerate(classe_dispo):
        print(f"{i+1}. {classe.nom}")
    choix = int(input("Entrez le numéro de la classe choisie: "))
    return classe_dispo[choix-1]

def recap_perso(personnage):
    print(f"Nom: {personnage.nom}")
    print(f"Classe: {personnage.Classe}")
    print(f"PV: {personnage.pv}")
    print(f"PM: {personnage.pm}")
    print(f"Force: {personnage.force}")
    print(f"Intelligence: {personnage.intelligence}")
    print(f"Défense: {personnage.défense}")
    print(f"Résistance magique: {personnage.résistance_magique}")
    print(f"Agilité: {personnage.agilité}")
    print(f"Chance: {personnage.chance}")
    print(f"Endurance: {personnage.endurance}")
    print(f"Esprit: {personnage.esprit}")

nom_personnage = nom_personnage()
classe = choix_classe()

perso = Personnage(nom_personnage, classe)
recap_perso(perso)
print("Personnage créé avec succès !")