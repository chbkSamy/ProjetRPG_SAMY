from plateau.controleur_deplacement import ControleurDeplacement
from plateau.grille import Grille
from .joueur import Joueur
from .gameView import GameView
from personnage.personnageFactory import PersonnageFactory
from personnage.classes import Classes

class Jeu:
    def __init__(self, view: GameView):
        self.view = view
        self._grille = Grille(largeur=5, hauteur=5)
        self._joueur = Joueur()
        self._controleur = ControleurDeplacement(self._joueur, self._grille)
        self._personnage = PersonnageFactory(Classes).creer_personnage()

    def demarrer(self):
        self.view.afficher(self._personnage.afficher_recapitulatif())
        self._boucle_principale()

    def _boucle_principale(self):
        while True:
            commande = self.view.demander_commande()

            if commande == 'Q':
                self.view.afficher("Fin du jeu.")
                break

            if commande in ['N', 'S', 'E', 'O']:
                message = self._controleur.executer_deplacement(commande)
                self.view.afficher(message)
            elif commande in ['G', 'D']:
                self._joueur.tourner(commande)
                self.view.afficher(f"Vous faites maintenant face à {self._joueur.direction.value}.")
            else:
                self.view.afficher("Commande non reconnue.")

            self.view.afficher(f"Statut -> Position : {self._joueur.position}, Orientation : {self._joueur.direction.value}")
