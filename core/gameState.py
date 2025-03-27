from plateau.controleur_deplacement import ControleurDeplacement
class GameState:
    def __init__(self):
        self.is_running = True

        
        self.grille = self._create_grille()
        self.joueur = self._create_joueur()
        self.controller = ControleurDeplacement(self.joueur, self.grille)
        self.personnage = self._create_personnage()

    def _create_grille(self):
        from plateau.grille import Grille
        return Grille(largeur=5, hauteur=5)

    def _create_joueur(self):
        from plateau.joueur import Joueur
        return Joueur()

    def _create_controleur(self):
        from plateau.controleur_deplacement import ControleurDeplacement
        return ControleurDeplacement(self.joueur, self.grille)

    def _create_personnage(self):
        from personnage.personnageFactory import PersonnageFactory
        from personnage.classes import Classes
        return PersonnageFactory(Classes).creer_personnage()
