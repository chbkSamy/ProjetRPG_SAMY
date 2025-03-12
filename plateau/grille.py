class Grille:
    def __init__(self, largeur=5, hauteur=5):
        self.largeur = largeur
        self.hauteur = hauteur

    def valider_position(self, x, y):
        """Vérifie si une position est valide sur la grille."""
        return 0 <= x < self.hauteur and 0 <= y < self.largeur
