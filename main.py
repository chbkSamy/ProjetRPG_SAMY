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

main()