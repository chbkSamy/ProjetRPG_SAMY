from classes import Classe

class Personnage (Classe):
    def __init__(self, nom_perso, Classe):
        super().__init__(Classe.nom, Classe.pv, Classe.pm, Classe.force, 
                     Classe.intelligence, Classe.défense, 
                     Classe.résistance_magique, Classe.agilité, 
                     Classe.chance, Classe.endurance, Classe.esprit)
        self.nom = nom_perso
        self.Classe = Classe.nom
    
