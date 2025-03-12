import random

class Combat:
    def __init__(self, joueur, monstre):
        self.joueur = joueur
        self.monstre = monstre
        self.joueur_pm_initial = joueur.stats.pm  # Sauvegarde les PM initiaux

    def _choisir_attaque(self):
        """Demande au joueur de choisir son type d'attaque."""
        while True:
            choix = input("Choisissez une attaque ([N]ormale/[M]agique) : ").upper()
            if choix == 'N':
                return 'physique'
            elif choix == 'M':
                if self.joueur.stats.pm >= 20:
                    return 'magique'
                else:
                    print("Pas assez de PM pour une attaque magique !")
            else:
                print("Choix invalide. Veuillez choisir N ou M.")

    def _calculer_degats(self, attaquant, defenseur, type_attaque):
        """Calcule les dégâts en fonction du type d'attaque et des stats."""
        # Calcul de base
        if type_attaque == 'physique':
            base_degats = attaquant.stats.force - defenseur.stats.defense
        else:  # magique
            base_degats = attaquant.stats.intelligence - defenseur.stats.resistance_magique

        # Application du minimum de dégâts
        degats = max(1, base_degats)

        # Calcul critique (basé sur la chance)
        if random.randint(1, 100) <= attaquant.stats.chance:
            degats *= 2
            print("Coup critique !")

        return degats

    def _tentative_esquive(self, defenseur):
        """Vérifie si le defenseur esquive l'attaque."""
        if random.randint(1, 100) <= defenseur.stats.chance:
            print(f"{defenseur.nom} esquive l'attaque !")
            return True
        return False

    def _tour_joueur(self):
        """Gère le tour du joueur."""
        type_attaque = self._choisir_attaque()

        if self._tentative_esquive(self.monstre):
            return

        degats = self._calculer_degats(self.joueur, self.monstre, type_attaque)

        # Consommation des PM pour les attaques magiques
        if type_attaque == 'magique':
            self.joueur.stats.pm -= 20
            print(f"Vous lancez un sort magique (-20 PM)")

        self.monstre.stats.pv -= degats
        print(f"Vous infligez {degats} dégâts ! PV restants du {self.monstre.nom}: {max(0, self.monstre.stats.pv)}")

    def _tour_monstre(self):
        """Gère le tour du monstre."""
        print(f"\nTour du {self.monstre.nom}...")

        if self._tentative_esquive(self.joueur):
            return

        degats = self._calculer_degats(self.monstre, self.joueur, 'physique')
        self.joueur.stats.pv -= degats
        print(f"Le {self.monstre.nom} vous inflige {degats} dégâts ! PV restants: {max(0, self.joueur.stats.pv)}")

    def lancer_combat(self):
        """Lance le combat complet."""
        print(f"\n=== COMBAT CONTRE {self.monstre.nom.upper()} ===")
        print(f"Vos PM: {self.joueur.stats.pm}")

        while self.joueur.stats.pv > 0 and self.monstre.stats.pv > 0:
            self._tour_joueur()
            if self.monstre.stats.pv <= 0:
                break

            self._tour_monstre()

        # Réinitialisation des PM après le combat
        self.joueur.stats.pm = self.joueur_pm_initial

        if self.joueur.stats.pv > 0:
            print(f"\nVictoire contre le {self.monstre.nom} !")
            return True
        else:
            print("\nDéfaite...")
            return False
