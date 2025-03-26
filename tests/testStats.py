import unittest
from personnage.stats import Stats

class TestStats(unittest.TestCase):
    def test_stats_values(self):
        stats = Stats(100, 200, 10, 15, 5, 6, 7, 8, 9, 10)
        self.assertEqual(stats.pv, 100)
        self.assertEqual(stats.pm, 200)
        self.assertEqual(stats.force, 10)
        self.assertEqual(stats.intelligence, 15)
        self.assertEqual(stats.defense, 5)
        self.assertEqual(stats.resistance_magique, 6)
        self.assertEqual(stats.agilite, 7)
        self.assertEqual(stats.chance, 8)
        self.assertEqual(stats.endurance, 9)
        self.assertEqual(stats.esprit, 10)


