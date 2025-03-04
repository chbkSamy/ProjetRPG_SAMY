import unittest
from unittest import mock
from classes.guerrier import Guerrier
from personnages import Personnage

class TestPersonnage(unittest.TestCase):
    
    def test_nom_personnage_valide(self):
        with mock.patch('builtins.input', return_value="TestNom"):
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertTrue(len(Personnage.nom_personnage())>=2 <=15)

    def test_nom_personnage_trop_court(self):
        with mock.patch('builtins.input', side_effect=["T", "TestNom"]):
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertTrue(len(Personnage.nom_personnage())>=2)

    def test_nom_personnage_trop_long(self):
        with mock.patch('builtins.input', side_effect=["UnNomQuiEstBeaucoupTropLong", "TestNom"]): 
            personnage = Personnage(nom_perso="", classe_perso=Guerrier())
            self.assertTrue(len(Personnage.nom_personnage())<=15)

if __name__ == '__main__':
    unittest.main()
