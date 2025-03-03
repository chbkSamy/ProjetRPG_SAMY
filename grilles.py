
class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]
        self.position_personnage = (0, 0)


    def initialiser_grille(self):
        for i in range(self.hauteur):
            for j in range(self.largeur):
                self.grille[i][j] = ' '

        self.position_personnage = (0, 0)

    def afficher_grille(self):
        for i in range(self.hauteur):
            for j in range(self.largeur):
                print(self.grille[i][j], end='')
            print()


   

