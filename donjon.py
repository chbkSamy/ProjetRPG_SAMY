import random

class Donjon:
    TAILLE = 6  # Taille du donjon (6x6)
    
    def __init__(self):
        """Initialisation du donjon avec un contenu aléatoire pour chaque salle."""
        self.grille = self.generer_donjon()

    def generer_donjon(self):
        """Génère une grille du donjon avec des salles contenant des monstres, des trésors ou rien."""
        elements = ["Vide", "Monstre", "Trésor", "Piège"]
        return [[random.choice(elements) for _ in range(self.TAILLE)] for _ in range(self.TAILLE)]

    def afficher_salle(self, x, y):
        """Retourne le contenu de la salle où se trouve le joueur."""
        return self.grille[y][x]

    def afficher_minimap(self, joueur_x, joueur_y):
        """Affiche une mini-map du donjon avec la position du joueur."""
        print("\n🗺️ Mini-Map du Donjon :")
        for y in range(self.TAILLE):
            for x in range(self.TAILLE):
                if x == joueur_x and y == joueur_y:
                    print("🧍", end=" ")  # Symbole du joueur
                else:
                    print("⬜", end=" ")  # Case inconnue
            print()

    def salle_contient_monstre(self, x, y):
        """Vérifie si la salle contient un monstre."""
        return self.grille[y][x] == "Monstre"

    def vider_salle(self, x, y):
        """Vide la salle après qu'un monstre a été vaincu ou qu'un trésor a été récupéré."""
        self.grille[y][x] = "Vide"
