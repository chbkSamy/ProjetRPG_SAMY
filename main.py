from personnages import Personnage

def main():

    choix_nom = Personnage.nom_personnage()
    selection_classe = Personnage.choix_classe()
    personnage = Personnage(nom_perso=choix_nom, classe_perso=selection_classe)
    personnage.recap_perso()

main()