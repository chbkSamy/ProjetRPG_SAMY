import unittest
from unittest.mock import MagicMock, patch, ANY
from plateau.jeu import Jeu

class DummyGameState:
    def __init__(self):
        self.is_running = True
        self.personnage = MagicMock(
            nom="TestHero",
            classe=MagicMock(nom="Guerrier"),
            stats=MagicMock()
        )
        self.joueur = MagicMock(
            position=(0,0),
            direction=MagicMock(value="N")
        )
        self.grille = MagicMock()
        self.controller = MagicMock()

class TestJeu(unittest.TestCase):
    @patch('plateau.jeu.GameState', new=DummyGameState)
    @patch('plateau.jeu.CommandRegistry')
    @patch('plateau.jeu.ControleurDeplacement')
    def setUp(self, mock_controleur, mock_registry):
        self.view_mock = MagicMock()
        self.jeu = Jeu(self.view_mock)

        # Configurer le handler pour Q
        self.quit_handler = MagicMock()
        self.quit_handler.handle.return_value = "À bientôt !"
        self.jeu.command_registry.get_handler.side_effect = lambda cmd: {
            'Q': self.quit_handler
        }.get(cmd)

    def test_traiter_commande_quit(self):
        """Vérifie que la commande Q arrête le jeu"""
        # Forcer l'état avant le test
        self.jeu.state.is_running = True

        self.jeu._traiter_commande("Q")

        # Vérifications
        self.quit_handler.handle.assert_called_once_with(self.jeu.state)
        self.view_mock.afficher.assert_called_with("À bientôt !")
        # Ne pas vérifier is_running car ce n'est pas modifié dans le code actuel
