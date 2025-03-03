from classes import Classes

class Personnage(Classes):
    def __init__(self, nom_personnage, classe):
        super().__init__(classe.nom, classe.pv, classe.pm, classe.force, classe.intelligence,
                         classe.defense, classe.resistance_magique, classe.agilite, classe.chance,
                         classe.endurance, classe.esprit)
        self.nom_personnage = nom_personnage
        self.classe = classe.nom


# def nom_personnage():
#     print("Le nom du personnage doit avoir entre 3 et 10 caractères.")
#     nom = input("Entrez le nom du personnage : ")
#     while len(nom) < 3 or len(nom) > 10:
#         print("Le nom du personnage doit avoir entre 3 et 10 caractères.")
#         nom = input("Entrez le nom du personnage : ")
#     return nom




# def recapitulatif_personnage(personnage):
#     print("Recapitulatif du personnage :")
#     print(f"Nom : {personnage.nom_personnage}")
#     print(f"Classe : {personnage.classe}")
#     print(f"PV : {personnage.pv}")
#     print(f"PM : {personnage.pm}")
#     print(f"Force : {personnage.force}")
#     print(f"Intelligence : {personnage.intelligence}")
#     print(f"Defense : {personnage.defense}")
#     print(f"Resistance magique : {personnage.resistance_magique}")
#     print(f"Agilité : {personnage.agilite}")
#     print(f"Chance : {personnage.chance}")
#     print(f"Endurance : {personnage.endurance}")
#     print(f"Esprit : {personnage.esprit}")
