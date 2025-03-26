import unittest
from plateau.gameView import GameView

class TestGameView(unittest.TestCase):
    def test_afficher(self):
        with unittest.mock.patch('builtins.print') as mocked_print:
            GameView.afficher("Test message")
            mocked_print.assert_called_with("Test message")
