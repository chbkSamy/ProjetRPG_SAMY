from .interface import CommandHandler

class MoveCommandHandler(CommandHandler):
    def __init__(self, direction: str):
        self.direction = direction

    def handle(self, game_state) -> str:
        return game_state.controller.executer_deplacement(self.direction)

class TurnCommandHandler(CommandHandler):
    def __init__(self, rotation: str):
        self.rotation = rotation

    def handle(self, game_state) -> str:
        game_state.joueur.tourner(self.rotation)
        return f"Orientation : {game_state.joueur.direction.value}"

class QuitCommandHandler(CommandHandler):
    def handle(self, game_state) -> str:
        game_state.is_running = False
        return "Au revoir !"
