import deplacement
import donjon
import personnages
from classes.classe import Classe
from personnages import Personnage
from grilles import Grille
from donjon import Donjon
from deplacement import Deplacement

def main():

    choix_nom = Personnage.nom_personnage()
    selection_classe = Personnage.choix_classe()
    personnage = Personnage(nom_perso=choix_nom, classe_perso=selection_classe)
    personnage.recap_perso()

    # while True:
    #     print(f"\n📍 Position: ({deplacement.x}, {deplacement.y}) - Orientation: {deplacement.directions[deplacement.orientation]}")
    #     print(f"📦 Contenu de la salle: {donjon.afficher_salle(deplacement.x, deplacement.y)}")
    #     print(f"⚔️ Personnage : {personnages.nom} | ❤️ PV : {personnages.pv}")

    #     # Affichage de la mini-map
    #     donjon.afficher_minimap(deplacement.x, deplacement.y)

    #     commande = input("🕹️ Commande (N/S/E/O/A/G/D) : ").upper()

    #     if commande in ["N", "S", "E", "O"]:
    #         deplacement.deplacer(commande)
    #     elif commande == "A":
    #         deplacement.avancer()
    #     elif commande == "G":
    #         deplacement.tourner_gauche()
    #     elif commande == "D":
    #         deplacement.tourner_droite()
    #     else:
    #         print("⚠️ Commande invalide.")

main()