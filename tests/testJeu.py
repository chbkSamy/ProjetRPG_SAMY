import unittest
from unittest.mock import patch
from plateau.jeu import Jeu

# Dummy implémentations pour simuler les dépendances

class DummyPersonnage:
    def afficher_recapitulatif(self):
        return "Recap dummy"

class DummyJoueur:
    def __init__(self):
        # On définit la position et la direction souhaitées pour le test
        self.position = (10, 20)
        # Simule une direction avec un attribut 'value'
        self.direction = type("DummyDirection", (), {"value": "N"})()

class DummyGrille:
    pass

class DummyGameState:
    def __init__(self):
        self.joueur = DummyJoueur()
        self.grille = DummyGrille()
        self.personnage = DummyPersonnage()
        self.is_running = False

class DummyCommandHandler:
    def handle(self, state):
        return "Command handled"

class DummyCommandRegistry:
    def __init__(self, handler=None):
        self.handler = handler
    def get_handler(self, commande):
        return self.handler

class DummyGameView:
    def __init__(self):
        self.messages = []
    def afficher(self, message: str):
        self.messages.append(message)
    def demander_commande(self):
        # Retourne "Q" pour quitter la boucle de jeu
        return "Q"

class TestJeu(unittest.TestCase):
    def setUp(self):
        self.view = DummyGameView()
        # Patch de builtins.input pour la création du personnage (via PersonnageFactory)
        patcher_input = patch('builtins.input', side_effect=["Test", "1"])
        self.mock_input = patcher_input.start()
        self.addCleanup(patcher_input.stop)
        # Patch de GameState et CommandRegistry dans le module plateau.jeu
        patcher_gs = patch('plateau.jeu.GameState', return_value=DummyGameState())
        patcher_cr = patch('plateau.jeu.CommandRegistry', return_value=DummyCommandRegistry())
        self.mock_game_state = patcher_gs.start()
        self.mock_command_registry = patcher_cr.start()
        self.addCleanup(patcher_gs.stop)
        self.addCleanup(patcher_cr.stop)
        # Instanciation de Jeu (les dépendances dummy sont désormais utilisées)
        self.jeu = Jeu(self.view)

    def test_afficher_introduction(self):
        """Vérifie que l'introduction affiche le récapitulatif et l'aide aux commandes."""
        self.jeu._afficher_introduction()
        combined = " ".join(self.view.messages)
        self.assertIn("Bienvenue dans l'aventure", combined)
        # On s'attend à retrouver le récapitulatif dummy
        self.assertIn("Recap dummy", combined)
        self.assertIn("Commandes disponibles:", combined)

    def test_traiter_commande_known(self):
        """Vérifie que lorsqu'un handler est trouvé, le résultat du handler est affiché."""
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
        self.jeu.state.is_running = True  # Activer la boucle de jeu
        with patch.object(self.view, 'demander_commande', side_effect=Exception("Test error")):
            self.jeu._run_game_loop()
        combined = " ".join(self.view.messages)
        self.assertIn("Erreur : Test error", combined)
        self.assertFalse(self.jeu.state.is_running)

