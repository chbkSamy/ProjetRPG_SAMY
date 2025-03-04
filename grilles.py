

class Grille:
    def __init__(self, largeur=5, hauteur=5):
        self.largeur = largeur
        self.hauteur = hauteur
        self.position_personnage = (0, 0)
        self.orientation = 'N'

    def _deplacer_vers(self, direction):
        directions = {
            'N': (-1, 0, 'Nord'),
            'S': (1, 0, 'Sud'),
            'E': (0, 1, 'Est'),
            'O': (0, -1, 'Ouest')
        }
        dx, dy, nom_dir = directions[direction]
        x, y = self.position_personnage
        new_x, new_y = x + dx, y + dy
        return (new_x, new_y), nom_dir

    def valider_deplacement(self, new_x, new_y):
        return 0 <= new_x < self.hauteur and 0 <= new_y < self.largeur

    def deplacer(self, commande):
        if commande in ['N', 'S', 'E', 'O']:
            new_pos, nom_dir = self._deplacer_vers(commande)
        elif commande == 'A':
            new_pos, nom_dir = self._deplacer_vers(self.orientation)
        else:
            return "Commande invalide."

        if self.valider_deplacement(*new_pos):
            self.position_personnage = new_pos
            return f"Vous vous déplacez vers le {nom_dir}. Nouvelle position : {self.position_personnage}"
        else:
            return f"Vous avez atteint le bord du monde. Vous ne pouvez pas aller plus au {nom_dir}."

    def tourner(self, direction):
        directions = ['N', 'E', 'S', 'O']
        idx = directions.index(self.orientation)
        if direction == 'G':
            self.orientation = directions[(idx - 1) % 4]
        elif direction == 'D':
            self.orientation = directions[(idx + 1) % 4]
        return f"Vous tournez à {direction}. Nouvelle orientation : {self.orientation}"

    def jouer(self):
        print("Bienvenue dans le jeu de déplacement sur grille !")
        print(f"Position initiale : {self.position_personnage}, Orientation : {self.orientation}")

        while True:
            commande = input("Entrez une commande (N, S, E, O, A, G, D) ou Q pour quitter : ").upper()
            if commande == 'Q':
                print("Merci d'avoir joué !")
                break
            elif commande in ['N', 'S', 'E', 'O', 'A']:
                resultat = self.deplacer(commande)
                print(resultat)
            elif commande in ['G', 'D']:
                resultat = self.tourner(commande)
                print(resultat)
            else:
                print("Commande invalide. Veuillez réessayer.")
