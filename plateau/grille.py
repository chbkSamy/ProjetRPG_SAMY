import random 

class Grille:
    def __init__(self, largeur=5, hauteur=5):
        self.largeur = largeur
        self.hauteur = hauteur
        self.monstres = {}

    def valider_position(self, x, y):
        return 0 <= x < self.hauteur and 0 <= y < self.largeur

    def ajouter_monstre(self, x, y, monstre):
        if self.valider_position(x, y):
            self.monstres[(x, y)] = monstre
        else:
            raise ValueError("Position invalide pour ajouter un monstre.")

    def obtenir_monstre(self, x, y):
        return self.monstres.get((x, y), None)

    def placer_monstres_aleatoires(self, nombre_monstres, liste_monstres):
        for _ in range(nombre_monstres):
            x = random.randint(0, self.hauteur - 1)
            y = random.randint(0, self.largeur - 1)
            monstre = random.choice(liste_monstres)
            self.ajouter_monstre(x, y, monstre)
