from personnage.personnage import Personnage
from plateau.jeu import Jeu
from plateau.gameView import GameView


if __name__ == "__main__":
    view = GameView()
    jeu = Jeu(view)
    jeu.demarrer()


