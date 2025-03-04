import unittest
from unittest import mock
from classes.guerrier import Guerrier
from personnages import Personnage

class TestPersonnage(unittest.TestCase):
    
    def test_nom_personnage_valide(self):
        with mock.patch('builtins.input', return_value="TestNom"):
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertEqual(Personnage.nom_personnage(), "TestNom")

    def test_nom_personnage_trop_court(self):
        with mock.patch('builtins.input', side_effect=["T", "TestNom"]):
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertEqual(Personnage.nom_personnage(), "TestNom")

    def test_nom_personnage_trop_long(self):
        with mock.patch('builtins.input', side_effect=["UnNomBeaucoupTropLong", "TestNom"]): 
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertEqual(Personnage.nom_personnage(), "TestNom")

if __name__ == '__main__':
    unittest.main()
