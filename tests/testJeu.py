import unittest
from unittest.mock import MagicMock, patch
from plateau.jeu import Jeu

class TestJeu(unittest.TestCase):
    def setUp(self):
        self.view = MagicMock()
        patcher = patch('builtins.input', side_effect=["Test", "1"])
        self.mock_input = patcher.start()
        self.addCleanup(patcher.stop)
        self.jeu = Jeu(self.view)

    def test_initialisation(self):
        self.assertIsNotNone(self.jeu._grille)
        self.assertIsNotNone(self.jeu._joueur)
        self.assertIsNotNone(self.jeu._controleur)
