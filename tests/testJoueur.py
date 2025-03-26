import unittest
from mouvement.direction import Direction
from mouvement.personnagemoove import CharacterMover
from plateau.joueur import Joueur

class TestJoueur(unittest.TestCase):
    def setUp(self):
        self.joueur = Joueur()

    def test_initialisation(self):
        self.assertEqual(self.joueur.mover.position, (0, 0))
        self.assertEqual(self.joueur.mover.direction, Direction('N'))

    def test_deplacement(self):

        new_pos = (3, 3)
        self.joueur.deplacer(new_pos)
        self.assertEqual(self.joueur.mover.position, new_pos)

    def test_tourner(self):
        self.joueur.tourner('D')
        self.assertEqual(self.joueur.mover.direction, Direction('E'))

