import unittest
from personnage.classes import Classes
from personnage.stats import Stats

class TestClasses(unittest.TestCase):
    def test_nom_des_classes(self):
        self.assertEqual(Classes.GUERRIER.nom, "Guerrier")
        self.assertEqual(Classes.MAGE.nom, "Mage")
        self.assertEqual(Classes.VOLEUR.nom, "Voleur")

    def test_stats_instance(self):
        self.assertIsInstance(Classes.GUERRIER.stats, Stats)
        self.assertIsInstance(Classes.MAGE.stats, Stats)
        self.assertIsInstance(Classes.VOLEUR.stats, Stats)
