import unittest
from mouvement.direction import Direction
from mouvement.personnagemoove import CharacterMover

class TestCharacterMover(unittest.TestCase):
    def setUp(self):
        self.mover = CharacterMover((0, 0), Direction('N'))

    def test_calculate_new_position(self):
        new_position = self.mover.calculate_new_position()
        self.assertEqual(new_position, (0, -1))

    def test_rotate_left(self):
        self.mover.rotate('G')
        self.assertEqual(self.mover.direction, Direction('O'))

    def test_rotate_right(self):
        self.mover.rotate('D')
        self.assertEqual(self.mover.direction, Direction('E'))


