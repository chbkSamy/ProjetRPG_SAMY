from personnage.personnage import Personnage
from personnage.personnageFactory import PersonnageFactory
from .joueur import Joueur
from .grille import Grille
from personnage.monstres import Monstres
from .controleur_deplacement import ControleurDeplacement
from personnage.classes import Classes
from .gameView import GameView

class Jeu:
    def __init__(self, view: GameView):
        self.view = view
        self._initialiser_components()

    def _initialiser_components(self):
        self._grille = Grille(largeur=5, hauteur=5)
        self._joueur = Joueur()
        self._controleur = ControleurDeplacement(self._joueur, self._grille)
        self._personnage = PersonnageFactory(Classes).creer_personnage()


        self._grille.generer_monstres_aleatoires(
            monstres_disponibles=[Monstres.SLIME, Monstres.DRAGON],
            nombre=3
        )

    def demarrer(self):
        self.view.afficher(self._personnage.afficher_recapitulatif())
        self._boucle_principale()

    def _boucle_principale(self):
        while True:
            commande = self.view.demander_commande()
            if commande == 'Q':
                self.view.afficher("Fin du jeu.")
                break
            elif commande in ['N', 'S', 'E', 'O']:
                message = self._controleur.executer_deplacement(commande)
                self.view.afficher(message)
            elif commande in ['G', 'D']:
                self._joueur.tourner(commande)
                self.view.afficher(f"Vous faites maintenant face à {self._joueur.orientation}.")
            else:
                self.view.afficher("Commande non reconnue.")


            self.view.afficher(f"Statut -> Position : {self._joueur.position}, Orientation : {self._joueur.orientation}")
