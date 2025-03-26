from mouvement.direction import Direction
from plateau.grille import Grille

class ControleurDeplacement:
    def __init__(self, joueur, grille: Grille):
        self.joueur = joueur
        self.grille = grille

    def executer_deplacement(self, direction: str) -> str:
        try:
            direction_enum = Direction(direction)
        except ValueError:
            return "Commande invalide."

        self.joueur.mover.direction = direction_enum
        new_pos = self.joueur.calculate_new_position()

        if not self._valider_deplacement(new_pos):
            return self._analyser_obstacle(new_pos)

        self.joueur.deplacer(new_pos)
        return self._analyser_contenu_case(new_pos)

    def _valider_deplacement(self, position: tuple[int, int]) -> bool:
        return self.grille.valider_position(*position)

    def _analyser_obstacle(self, position: tuple[int, int]) -> str:
        x, y = position
        if not self.grille.valider_position(x, y):
            return "Bord du monde atteint !"
        if self.grille.obtenir_obstacle(x, y):
            return "Obstacle détecté !"
        if self.grille.obtenir_monstre(x, y):
            return "Monstre en vue !"
        return ""

    def _analyser_contenu_case(self, position: tuple[int, int]) -> str:
        tresor = self.grille.obtenir_tresor(*position)
        return f"Trésor {tresor.nom} trouvé !" if tresor else "Déplacement réussi"
