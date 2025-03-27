import unittest
from unittest.mock import patch
from plateau.jeu import Jeu

# Dummy handler et registry pour simuler le comportement du registre de commandes
class DummyCommandHandler:
    def handle(self, state):
        return "Command handled"

class DummyCommandRegistry:
    def __init__(self, handler=None):
        self.handler = handler
    def get_handler(self, commande):
        return self.handler

# Dummy GameState pour simuler l'état du jeu
class DummyGameState:
    def __init__(self):
        from collections import namedtuple
        DummyDirection = namedtuple("DummyDirection", ["value"])
        # Création d'un dummy joueur avec position et direction
        DummyJoueur = type("DummyJoueur", (), {})()
        DummyJoueur.position = (10, 20)
        DummyJoueur.direction = DummyDirection("N")
        self.joueur = DummyJoueur
        self.grille = None  # Non utilisé dans ces tests
        # Dummy personnage pour le récapitulatif
        class DummyPersonnage:
            def afficher_recapitulatif(self):
                return "Recap dummy"
        self.personnage = DummyPersonnage()
        self.is_running = False  # Par défaut, pour éviter la boucle infinie

# Dummy GameView pour capturer les messages affichés et simuler input
class DummyGameView:
    def __init__(self):
        self.messages = []
    def afficher(self, message: str):
        self.messages.append(message)
    def demander_commande(self):
        return "Q"  # Retourne "Q" pour quitter la boucle de jeu

class TestJeu(unittest.TestCase):
    def setUp(self):
        self.view = DummyGameView()
        # Patch de GameState et CommandRegistry dans leurs modules d'origine
        patcher_gs = patch('core.gameState.GameState', return_value=DummyGameState())
        patcher_cr = patch('core.registry.CommandRegistry', return_value=DummyCommandRegistry())
        self.mock_game_state = patcher_gs.start()
        self.mock_command_registry = patcher_cr.start()
        self.addCleanup(patcher_gs.stop)
        self.addCleanup(patcher_cr.stop)
        # Instanciation de Jeu avec la vue dummy
        self.jeu = Jeu(self.view)

    def test_afficher_introduction(self):
        """Vérifie que l'introduction affiche le récapitulatif et l'aide aux commandes."""
        self.jeu._afficher_introduction()
        combined = " ".join(self.view.messages)
        self.assertIn("Bienvenue dans l'aventure", combined)
        self.assertIn("Recap dummy", combined)
        self.assertIn("Commandes disponibles:", combined)

    def test_traiter_commande_known(self):
        """Vérifie que lorsqu'un handler est connu, le résultat du handler est affiché."""
        dummy_handler = DummyCommandHandler()
        self.jeu.command_registry = DummyCommandRegistry(handler=dummy_handler)
        self.view.messages = []  # Réinitialiser les messages
        self.jeu._traiter_commande("any")
        self.assertIn("Command handled", self.view.messages)

    def test_traiter_commande_unknown(self):
        """Vérifie que lorsqu'aucun handler n'est trouvé, un message d'erreur et l'aide sont affichés."""
        self.jeu.command_registry = DummyCommandRegistry(handler=None)
        self.view.messages = []
        self.jeu._traiter_commande("any")
        combined = " ".join(self.view.messages)
        self.assertIn("Commande non reconnue", combined)
        self.assertIn("Commandes disponibles:", combined)

    def test_afficher_statut(self):
        """Vérifie que le statut affiché correspond à la position et à l'orientation du joueur dummy."""
        self.view.messages = []
        self.jeu._afficher_statut()
        combined = " ".join(self.view.messages)
        self.assertIn("Position: (10, 20)", combined)
        self.assertIn("Orientation: N", combined)

    def test_run_game_loop_exception(self):
        """Simule une exception lors de la demande de commande pour vérifier la gestion d'erreur."""
        self.jeu.state.is_running = True  # Activer la boucle
        with patch.object(self.view, 'demander_commande', side_effect=Exception("Test error")):
            self.jeu._run_game_loop()
        combined = " ".join(self.view.messages)
        self.assertIn("Erreur : Test error", combined)
        self.assertFalse(self.jeu.state.is_running)

