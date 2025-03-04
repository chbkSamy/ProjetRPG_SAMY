from personnage.personnage import Personnage
from grilles import Grille


if __name__ == "__main__":

    personnage = Personnage.initialiser_personnage()
    personnage.recapitulatif_personnage()
    grille = Grille()
    grille.jouer()

