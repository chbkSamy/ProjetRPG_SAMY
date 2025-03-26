from .interfaces import Positionnable
from .grille import Grille

class ControleurDeplacement:
    def __init__(self, joueur: Positionnable, grille: Grille):
        self._joueur = joueur
        self._grille = grille

    def executer_deplacement(self, commande: str) -> str:
        if commande in ['N', 'S', 'E', 'O']:
            self._joueur.set_orientation(commande)
        else:
            return "Commande invalide."

        dx, dy = self._joueur.get_orientation_vecteur()
        x, y = self._joueur.position
        new_x = x + dx
        new_y = y + dy
        direction = self._joueur.orientation

        if not self._grille.valider_position(new_x, new_y):
            return f"Vous avez atteint le bord du monde. Vous ne pouvez pas aller plus au {direction}."

        if self._grille.obtenir_obstacle(new_x, new_y):
            return "Un obstacle vous bloque le passage. Vous ne pouvez pas aller par là."

        if self._grille.obtenir_monstre(new_x, new_y):
            return "Un monstre bloque votre chemin ! Vous devez le vaincre pour avancer."

        tresor = self._grille.obtenir_tresor(new_x, new_y)
        if tresor:
            self._joueur.deplacer(new_x, new_y)
            self._joueur.inventaire.append(tresor)
            return f"Vous avez trouvé un trésor en position {self._joueur.position} !"

        self._joueur.deplacer(new_x, new_y)
        return f"Vous êtes maintenant en position {self._joueur.position}."
