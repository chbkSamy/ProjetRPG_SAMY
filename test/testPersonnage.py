import unittest
from unittest import mock
from personnage.personnage import Personnage
from personnage.classes import Classes

class TestPersonnageNomValidation(unittest.TestCase):
    def test_nom_valide(self):
        personnage = Personnage("Hector", Classes.GUERRIER)
        self.assertEqual(personnage.nom, "Hector")

class TestClassesProperties(unittest.TestCase):
    def test_nom_property(self):
        self.assertEqual(Classes.GUERRIER.nom, "Guerrier")
        self.assertEqual(Classes.MAGE.nom, "Mage")
        self.assertEqual(Classes.VOLEUR.nom, "Voleur")

    def test_stats_property(self):
        self.assertEqual(Classes.GUERRIER.stats.pv, 150)
        self.assertEqual(Classes.MAGE.stats.pm, 150)
        self.assertEqual(Classes.VOLEUR.stats.agilite, 15)

class TestPersonnageInitialisation(unittest.TestCase):
    def test_initialiser_personnage_nom_valide(self):
        # Simuler une entrée utilisateur
        with mock.patch('builtins.input', side_effect=["Hector", "1"]):
            personnage = Personnage.initialiser_personnage()
            self.assertEqual(personnage.nom, "Hector")
            self.assertEqual(personnage.classe, Classes.GUERRIER)

    def test_initialiser_personnage_nom_invalide(self):
        # Simuler une entrée utilisateur avec un nom invalide suivi d'un nom valide
        with mock.patch('builtins.input', side_effect=["He", "Hector", "1"]):
            personnage = Personnage.initialiser_personnage()
            self.assertEqual(personnage.nom, "Hector")
            self.assertEqual(personnage.classe, Classes.GUERRIER)

class TestPersonnageRecapitulatif(unittest.TestCase):
    def test_recapitulatif_personnage(self):
        guerrier = Personnage("Hector", Classes.GUERRIER)
        with mock.patch('builtins.print') as mocked_print:
            guerrier.recapitulatif_personnage()
            # Vérifiez que les informations du personnage sont bien affichées
            mocked_print.assert_any_call("Nom : Hector")
            mocked_print.assert_any_call("Classe : Guerrier")
            mocked_print.assert_any_call("PV : 150")
            mocked_print.assert_any_call("Force : 15")

class TestClassesStats(unittest.TestCase):
    def test_guerrier_stats(self):
        guerrier = Personnage("Hector", Classes.GUERRIER)
        self.assertEqual(guerrier.stats.pv, 150)
        self.assertEqual(guerrier.stats.force, 15)
        self.assertEqual(guerrier.stats.defense, 12)

    def test_mage_stats(self):
        mage = Personnage("Merlin", Classes.MAGE)
        self.assertEqual(mage.stats.pv, 90)
        self.assertEqual(mage.stats.pm, 150)
        self.assertEqual(mage.stats.intelligence, 15)

    def test_voleur_stats(self):
        voleur = Personnage("Lupin", Classes.VOLEUR)
        self.assertEqual(voleur.stats.agilite, 15)
        self.assertEqual(voleur.stats.chance, 12)


