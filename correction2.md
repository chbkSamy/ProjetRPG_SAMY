# Infractions aux Principes SOLID

## Single Responsibility Principle (SRP)

1. **Classe Combat** (`combat/combat.py`)
   ```python
   class Combat:
       def __init__(self, joueur, monstre):
           self.joueur = joueur
           self.monstre = monstre
           self.joueur_pm_initial = joueur.stats.pm

       def _choisir_attaque(self):  # Responsabilité d'interface utilisateur
           while True:
               choix = input("Choisissez une attaque ([N]ormale/[M]agique) : ").upper()
               # ...

       def _calculer_degats(self, attaquant, defenseur, type_attaque):  # Responsabilité de calcul
           if type_attaque == 'physique':
               base_degats = attaquant.stats.force - defenseur.stats.defense
           else:  # magique
               base_degats = attaquant.stats.intelligence - defenseur.stats.resistance_magique
           # ...

       def _tour_joueur(self):  # Responsabilité de gestion de tour
           type_attaque = self._choisir_attaque()
           if self._tentative_esquive(self.monstre):
               return
           # ...

       def lancer_combat(self):  # Responsabilité de gestion de combat
           print(f"\n=== COMBAT CONTRE {self.monstre.nom.upper()} ===")
           # ...
   ```

2. **Classe Personnage** (`personnage/personnage.py`)
   ```python
   class Personnage:
       def __init__(self, nom: str, classe: ClasseProvider):
           self.nom = nom
           self.classe = classe
           self.stats = classe.stats

       def afficher_recapitulatif(self) -> str:  # Responsabilité d'affichage
           return "\n".join([
               "\n=== Récapitulatif du personnage ===",
               f"Nom : {self.nom}",
               # ...
           ])
   ```

## Open/Closed Principle (OCP)

1. **Choix d'Attaque** (`combat/combat.py`)
   ```python
   def _choisir_attaque(self):
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
   # Modification nécessaire pour ajouter de nouveaux types d'attaques
   ```

2. **Calcul des Dégâts** (`combat/combat.py`)
   ```python
   def _calculer_degats(self, attaquant, defenseur, type_attaque):
       if type_attaque == 'physique':
           base_degats = attaquant.stats.force - defenseur.stats.defense
       else:  # magique
           base_degats = attaquant.stats.intelligence - defenseur.stats.resistance_magique
   # Modification nécessaire pour ajouter de nouveaux types de dégâts
   ```

3. **Gestion des PM** (`combat/combat.py`)
   ```python
   def _tour_joueur(self):
       # ...
       if type_attaque == 'magique':
           self.joueur.stats.pm -= 20
           print(f"Vous lancez un sort magique (-20 PM)")
   # Modification nécessaire pour ajouter de nouveaux coûts en PM
   ```

## Liskov Substitution Principle (LSP)

1. **Combat** (`combat/combat.py`)
   ```python
   def _tour_monstre(self):
       degats = self._calculer_degats(self.monstre, self.joueur, 'physique')
       # Le monstre est forcé d'utiliser une attaque physique
   ```

## Interface Segregation Principle (ISP)

1. **Dépendances Forcées** (`combat/combat.py`)
   ```python
   def _choisir_attaque(self):
       while True:
           choix = input("Choisissez une attaque ([N]ormale/[M]agique) : ").upper()
           # Forcé d'implémenter toutes les options d'attaque
   ```

## Dependency Inversion Principle (DIP)

1. **Dépendances Concrètes** (`combat/combat.py`)
   ```python
   def __init__(self, joueur, monstre):
       self.joueur = joueur
       self.monstre = monstre
       self.joueur_pm_initial = joueur.stats.pm
   # Dépendance directe vers les implémentations concrètes
   ```

2. **Injection de Dépendances** (`personnage/personnage.py`)
   ```python
   def __init__(self, nom: str, classe: ClasseProvider):
       self.nom = nom
       self.classe = classe
       self.stats = classe.stats
   # Dépendance directe vers ClasseProvider
   ``` 
