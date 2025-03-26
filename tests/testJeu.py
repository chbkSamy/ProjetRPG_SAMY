import unittest
from unittest.mock import MagicMock
from plateau.jeu import Jeu
class TestJeu(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock()
        self.jeu = Jeu(self.view)

    def test_initialisation(self):
        self.assertIsNotNone(self.jeu._grille)
        self.assertIsNotNone(self.jeu._joueur)
        self.assertIsNotNone(self.jeu._controleur)
