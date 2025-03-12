from personnage.personnage import Personnage
from .joueur import Joueur
from .grille import Grille
from .monstres import Monstres
from .controleur_deplacement import ControleurDeplacement
class Jeu:
    def __init__(self):
        self.personnage = Personnage.initialiser_personnage()
        self.joueur = Joueur()
        self.grille = Grille()
        self.controleur = ControleurDeplacement(self.joueur, self.grille)


        self.liste_monstres = [Monstres.SLIME, Monstres.DRAGON]


        self.grille.placer_monstres_aleatoires(nombre_monstres=3, liste_monstres=self.liste_monstres)

    def jouer(self):
        """Lance le jeu et gère les interactions utilisateur."""
        print("Bienvenue dans le jeu de déplacement sur grille !")
        self.personnage.recapitulatif_personnage()
        print(f"Position initiale : {self.joueur.get_position()}, Orientation : {self.joueur.get_orientation()}")

        while True:
            commande = input("Entrez une commande (N, S, E, O, A, G, D) ou Q pour quitter : ").upper()
            if commande == 'Q':
                print("Merci d'avoir joué !")
                break
            elif commande in ['N', 'S', 'E', 'O', 'A']:
                print(self.controleur.executer_deplacement(commande))
            elif commande in ['G', 'D']:
                print(self.joueur.tourner(commande))
            else:
                print("Commande invalide. Veuillez réessayer.")
