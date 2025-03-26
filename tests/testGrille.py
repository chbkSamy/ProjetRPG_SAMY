import unittest
from plateau.grille import Grille

class TestGrille(unittest.TestCase):
    def setUp(self):
        self.grille = Grille(5, 5)

    def test_position_valide(self):
        self.assertTrue(self.grille.valider_position(2, 2))
        self.assertFalse(self.grille.valider_position(5, 5))

