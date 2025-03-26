import unittest
from plateau.joueur import Joueur

class TestJoueur(unittest.TestCase):
    def setUp(self):
        self.joueur = Joueur()

    def test_initialisation(self):
        self.assertEqual(self.joueur.position, (0, 0))
        self.assertEqual(self.joueur.orientation, 'N')

    def test_deplacement(self):
        self.joueur.deplacer(3, 3)
        self.assertEqual(self.joueur.position, (3, 3))

    def test_tourner(self):
        self.joueur.tourner('D')
        self.assertEqual(self.joueur.orientation, 'E')
        self.joueur.tourner('G')
        self.assertEqual(self.joueur.orientation, 'N')



