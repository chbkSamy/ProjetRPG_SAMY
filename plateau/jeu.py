# plateau/jeu.py
from core.gameState import GameState
from .gameView import GameView
from core.registry import CommandRegistry
from plateau.controleur_deplacement import ControleurDeplacement
from personnage.recapGenerator import PersonnageRecapGenerator

class Jeu:
    def __init__(self, view: GameView):
        self.view = view
        self.state = GameState()
        self.command_registry = CommandRegistry()

        self._controleur = ControleurDeplacement(
            self.state.joueur,
            self.state.grille
        )

    def demarrer(self):
        """Démarre le jeu avec la boucle principale"""
        self._afficher_introduction()
        self._run_game_loop()

    def _afficher_introduction(self):
        """Affiche les informations initiales du jeu"""
        recap = PersonnageRecapGenerator.generer_recapitulatif(
            self.state.personnage.nom,
            self.state.personnage.classe.nom,
            self.state.personnage.stats
        )

        intro = f"""
        Bienvenue dans l'aventure !
        {recap}
        """
        self.view.afficher(intro)
        self._afficher_aide_commandes()

    def _run_game_loop(self):
        """Boucle principale du jeu"""
        while self.state.is_running:
            try:
                commande = self.view.demander_commande()
                self._traiter_commande(commande)
                self._afficher_statut()

            except Exception as e:
                self.view.afficher(f"Erreur : {str(e)}")
                self.state.is_running = False

    def _traiter_commande(self, commande: str):
        """Traite une commande utilisateur"""
        handler = self.command_registry.get_handler(commande)

        if handler:
            result = handler.handle(self.state)
            self.view.afficher(result)
        else:
            self.view.afficher("Commande non reconnue")
            self._afficher_aide_commandes()

    def _afficher_statut(self):
        """Affiche le statut actuel du joueur"""
        statut = (
            f"Position: {self.state.joueur.position}\n"
            f"Orientation: {self.state.joueur.direction.value}"
        )
        self.view.afficher(statut)

    def _afficher_aide_commandes(self):
        """Affiche l'aide des commandes disponibles"""
        aides = [
            "Commandes disponibles:",
            "N/S/E/O - Déplacement",
            "G/D - Rotation",
            "Q - Quitter"
        ]
        self.view.afficher('\n'.join(aides))
