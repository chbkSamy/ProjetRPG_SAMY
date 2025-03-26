import unittest
from mouvement.direction import Direction
from mouvement.moovementStrategies import NorthMovement, EastMovement, SouthMovement, WestMovement

class TestMovementStrategies(unittest.TestCase):
    def test_north_movement(self):
        movement = NorthMovement()
        self.assertEqual(movement.get_vector(), (0, -1))

    def test_east_movement(self):
        movement = EastMovement()
        self.assertEqual(movement.get_vector(), (1, 0))

    def test_south_movement(self):
        movement = SouthMovement()
        self.assertEqual(movement.get_vector(), (0, 1))

    def test_west_movement(self):
        movement = WestMovement()
        self.assertEqual(movement.get_vector(), (-1, 0))

