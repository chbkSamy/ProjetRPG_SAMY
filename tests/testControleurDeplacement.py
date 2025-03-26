import unittest
from unittest.mock import MagicMock
from mouvement.direction import Direction
from plateau.grille import Grille
from plateau.controleur_deplacement import ControleurDeplacement

class TestControleurDeplacement(unittest.TestCase):
    def setUp(self):
        self.joueur = MagicMock()
        self.joueur.calculate_new_position.return_value = (1, 1)
        self.grille = MagicMock(spec=Grille)
        self.controleur = ControleurDeplacement(self.joueur, self.grille)

    def test_executer_deplacement_valid(self):
        self.grille.valider_position.return_value = True
        self.grille.obtenir_tresor.return_value = None

        result = self.controleur.executer_deplacement('N')
        self.assertEqual(result, "Déplacement réussi")

    def test_executer_deplacement_invalid_direction(self):
        result = self.controleur.executer_deplacement('INVALID')
        self.assertEqual(result, "Commande invalide.")

    def test_executer_deplacement_obstacle(self):
        self.grille.valider_position.return_value = False
        result = self.controleur.executer_deplacement('N')
        self.assertEqual(result, "Bord du monde atteint !")
