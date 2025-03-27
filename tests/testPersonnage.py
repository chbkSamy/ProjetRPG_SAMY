import unittest
from unittest.mock import Mock, patch
from personnage.personnage import Personnage
from personnage.classes import Classes
from personnage.personnageFactory import PersonnageFactory
from personnage.recapGenerator import PersonnageRecapGenerator

class TestPersonnage(unittest.TestCase):
    def test_personnage_attributes(self):
        """Vérifie la présence des attributs requis"""
        # Configuration mock
        classe_mock = Mock()
        classe_mock.nom = "Guerrier"
        classe_mock.stats = Mock(
            pv=100, pm=50, force=15, intelligence=10,
            defense=20, resistance_magique=5,
            agilite=10, chance=5, endurance=15, esprit=8
        )

        # Test
        perso = Personnage("Héros", classe_mock)

        # Vérifications
        self.assertEqual(perso.nom, "Héros")
        self.assertEqual(perso.classe.nom, "Guerrier")
        self.assertIsNotNone(perso.stats)

    def test_recap_generation(self):
        """Vérifie la génération du récapitulatif"""
        # Configuration mock
        classe_mock = Mock()
        classe_mock.nom = "Mage"
        classe_mock.stats = Mock(
            pv=80, pm=100, force=5, intelligence=20,
            defense=10, resistance_magique=15,
            agilite=8, chance=10, endurance=12, esprit=18
        )

        perso = Personnage("Merlin", classe_mock)

        # Génération recap
        recap = PersonnageRecapGenerator.generer_recapitulatif(
            perso.nom,
            perso.classe.nom,
            perso.stats
        )

        # Vérifications
        self.assertIn("Merlin", recap)
        self.assertIn("Mage", recap)
        self.assertIn("PV : 80", recap)

