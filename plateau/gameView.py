class GameView:
    @staticmethod
    def afficher(message: str):
        print(message)

    @staticmethod
    def demander_commande() -> str:
        return input("Commande (N/S/E/O pour se déplacer, G/D pour tourner, Q pour quitter) : ").upper()
