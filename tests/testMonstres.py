import unittest
from personnage.monstres import Monstres
from personnage.stats import Stats

class TestMonstres(unittest.TestCase):
    def test_nom_des_monstres(self):
        self.assertEqual(Monstres.SLIME.nom, "Slime")
        self.assertEqual(Monstres.SQUELETTE.nom, "Squelette")
        self.assertEqual(Monstres.DRAGON.nom, "Dragon")

    def test_stats_instance(self):
        self.assertIsInstance(Monstres.SLIME.stats, Stats)
        self.assertIsInstance(Monstres.SQUELETTE.stats, Stats)
        self.assertIsInstance(Monstres.DRAGON.stats, Stats)
