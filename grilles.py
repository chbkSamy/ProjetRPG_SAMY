import random

class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = self.generer_grille()

    def generer_grille(self):
        return [[random.choice([" ", "M", "T", "1"]) for _ in range(self.largeur)] for _ in range(self.hauteur)]
    
    def afficher_grille(self, joueur_x, joueur_y):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if x == joueur_x and y == joueur_y:
                    print("👾", end=" ")
                else:
                    print(self.grille[y][x], end=" ")
            print()
