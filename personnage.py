from classes import Classes

class Personnage(Classes):
    def __init__(self, nom_personnage, classe):
        super().__init__(classe.nom, classe.pv, classe.pm, classe.force, classe.intelligence,
                         classe.defense, classe.resistance_magique, classe.agilite, classe.chance,
                         classe.endurance, classe.esprit)
        self.nom_personnage = nom_personnage
        self.classe = classe.nom



