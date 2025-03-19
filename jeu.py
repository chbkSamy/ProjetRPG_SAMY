from personnages import Personnage
from deplacement import Deplacement
from donjon import Donjon

class Jeu:
    def __init__(self):
        self.donjon = Donjon() 
        self.personnage = Personnage(nom_perso=Personnage.nom_personnage(), classe_perso=Personnage.choix_classe())
        self.deplacement = Deplacement(self.personnage, self.donjon.TAILLE, self.donjon.TAILLE)

    def jouer(self):
        """Boucle principale du jeu"""
        while True:
            print(f"\n📍 Position : ({self.deplacement.x}, {self.deplacement.y}) - Orientation : {Deplacement.DIRECTIONS[self.deplacement.orientation]} - ❤️ {self.personnage.pv} PV")
            print(f"📦 Contenu de la salle : {self.donjon.afficher_salle(self.deplacement.x, self.deplacement.y)}")

            self.donjon.afficher_minimap(self.deplacement.x, self.deplacement.y)

            commande = input("🕹️ Commande (N/S/E/O/A/G/D) : ").upper()
            if commande in ["N", "S", "E", "O"]:
                self.deplacement.deplacer(commande)
            elif commande == "A":
                self.deplacement.avancer()
            elif commande == "G":
                self.deplacement.tourner_gauche()
            elif commande == "D":
                self.deplacement.tourner_droite()
            else:
                print("⚠️ Commande invalide.")
