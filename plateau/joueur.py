class Joueur:
    def __init__(self, position=(0, 0), orientation='N'):
        self.position = position
        self.orientation = orientation
        self.directions = ['N', 'E', 'S', 'O']

    def tourner(self, direction):
        """Gère la rotation du joueur."""
        idx = self.directions.index(self.orientation)
        if direction == 'G':
            self.orientation = self.directions[(idx - 1) % 4]
        elif direction == 'D':
            self.orientation = self.directions[(idx + 1) % 4]
        return f"Vous tournez à {direction}. Nouvelle orientation : {self.orientation}"

    def get_orientation(self):
        return self.orientation

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
