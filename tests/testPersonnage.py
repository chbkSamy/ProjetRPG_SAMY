import unittest
from unittest.mock import patch
from unittest import mock
from personnage.personnage import Personnage
from personnage.classes import Classes
from personnage.personnageFactory import PersonnageFactory

class TestPersonnage(unittest.TestCase):
    def test_afficher_recapitulatif(self):
        nom = "Hero"
        personnage = Personnage(nom, Classes.GUERRIER)
        recap = personnage.afficher_recapitulatif()

        self.assertIn("Nom : Hero", recap)
        self.assertIn("Classe : Guerrier", recap)
        self.assertIn("PV :", recap)
        self.assertIn("Force :", recap)


class TestPersonnageFactory(unittest.TestCase):
    @patch('builtins.input', side_effect=["Hero", "1"])
    def test_creer_personnage_valide(self, mock_input):

        factory = PersonnageFactory([Classes.GUERRIER, Classes.MAGE, Classes.VOLEUR])
        personnage = factory.creer_personnage()

        self.assertIsInstance(personnage, Personnage)
        self.assertEqual(personnage.nom, "Hero")
        self.assertEqual(personnage.classe.nom, "Guerrier")

    @patch('builtins.input', side_effect=["He", "Hero123", "2"])
    def test_nom_invalide_puis_valide(self, mock_input):

        factory = PersonnageFactory([Classes.GUERRIER, Classes.MAGE, Classes.VOLEUR])
        personnage = factory.creer_personnage()

        self.assertEqual(personnage.nom, "Hero123")
        self.assertEqual(personnage.classe.nom, "Mage")
