from classes import Classes
from personnage import Personnage


guerrier = Classes("Guerrier", 150, 150, 15, 5, 12, 6, 8, 5, 10, 4)
mage = Classes("Mage", 90, 150, 4, 15, 5, 12, 7, 6, 5, 10)
voleur = Classes("Voleur", 110, 70, 10, 7, 8, 7, 15, 12, 7, 6)
classes_disponibles = [guerrier, mage, voleur]

def nom_personnage():
    print("Le nom du personnage doit avoir entre 3 et 10 caractères.")
    nom = input("Entrez le nom du personnage : ")
    while len(nom) < 3 or len(nom) > 10:
        print("Le nom du personnage doit avoir entre 3 et 10 caractères.")
        nom = input("Entrez le nom du personnage : ")
    return nom

def selection_classe():
    print("Choisissez une classe :")
    for i, classe in enumerate(classes_disponibles):
        print(f"{i + 1}. {classe.nom}")
    choix = int(input("Entrez le numéro de la classe choisie : "))
    return classes_disponibles[choix - 1]


def recapitulatif_personnage(personnage):
    print("Recapitulatif du personnage :")
    print(f"Nom : {personnage.nom_personnage}")
    print(f"Classe : {personnage.classe}")
    print(f"PV : {personnage.pv}")
    print(f"PM : {personnage.pm}")
    print(f"Force : {personnage.force}")
    print(f"Intelligence : {personnage.intelligence}")
    print(f"Defense : {personnage.defense}")
    print(f"Resistance magique : {personnage.resistance_magique}")
    print(f"Agilité : {personnage.agilite}")
    print(f"Chance : {personnage.chance}")
    print(f"Endurance : {personnage.endurance}")
    print(f"Esprit : {personnage.esprit}")

nom_personnage = nom_personnage()
classe_personnage = selection_classe()

personnage = Personnage(nom_personnage, classe_personnage)

recapitulatif_personnage(personnage)
