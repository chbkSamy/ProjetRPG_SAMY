class ControleurDeplacement:
    def __init__(self, joueur, grille):
        self.joueur = joueur
        self.grille = grille
        self.vecteurs = {
            'N': (-1, 0, 'Nord'),
            'S': (1, 0, 'Sud'),
            'E': (0, 1, 'Est'),
            'O': (0, -1, 'Ouest')
        }

    def _calculer_trajectoire(self, direction):
        dx, dy, nom = self.vecteurs[direction]
        x, y = self.joueur.get_position()
        return (x + dx, y + dy), nom

    def executer_deplacement(self, commande):
        if commande == 'A':
            direction = self.joueur.get_orientation()
        elif commande in self.vecteurs:
            direction = commande
        else:
            return "Commande invalide."

        nouvelle_pos, nom_direction = self._calculer_trajectoire(direction)

        if self.grille.valider_position(*nouvelle_pos):
            monstre = self.grille.obtenir_monstre(*nouvelle_pos)
            if monstre:
                return f"Vous avez croisé un monstre : {monstre.nom} !"
            else:
                self.joueur.set_position(nouvelle_pos)
                return f"Vous vous déplacez vers le {nom_direction}. Nouvelle position : {self.joueur.get_position()}"
        else:
            return f"Vous avez atteint le bord. Impossible d'aller au {nom_direction}."
