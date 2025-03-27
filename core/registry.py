from .handlers import MoveCommandHandler, TurnCommandHandler, QuitCommandHandler

class CommandRegistry:
    def __init__(self):
        self.handlers = {
            'N': lambda: MoveCommandHandler('N'),
            'S': lambda: MoveCommandHandler('S'),
            'E': lambda: MoveCommandHandler('E'),
            'O': lambda: MoveCommandHandler('O'),
            'G': lambda: TurnCommandHandler('G'),
            'D': lambda: TurnCommandHandler('D'),
            'Q': lambda: QuitCommandHandler()
        }

    def get_handler(self, command: str):
        return self.handlers.get(command.upper(), lambda: None)()
