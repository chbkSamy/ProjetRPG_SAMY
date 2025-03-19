## Violations des Principes SOLID

### Single Responsibility Principle (SRP)
- La classe `Personnage` viole le SRP en gérant à la fois :
  - La création du personnage (nom_personnage, choix_classe)
  - L'affichage des informations (recap_perso)
  - La logique d'attaque (attaquer)
  - L'interaction utilisateur (nom_personnage, choix_classe)

- La classe `Jeu` viole le SRP en gérant :
  - L'initialisation du jeu
  - La boucle de jeu
  - L'affichage
  - La gestion des commandes

### Open/Closed Principle (OCP)
- La classe `Classe` n'est pas extensible pour de nouveaux types de classes sans modification
- La méthode `attaquer` dans `Personnage` est trop simple et ne permet pas d'extension pour différents types d'attaques

### Liskov Substitution Principle (LSP)
- La classe `Personnage` hérite de `Classe` mais ne respecte pas complètement le contrat de la classe parente
- Les méthodes statiques dans `Personnage` ne respectent pas le principe de substitution

### Interface Segregation Principle (ISP)
- La classe `Classe` force toutes les classes à implémenter tous les attributs, même s'ils ne sont pas nécessaires
- Pas d'interfaces définies pour séparer les responsabilités

### Dependency Inversion Principle (DIP)
- La classe `Jeu` dépend directement des implémentations concrètes plutôt que d'abstractions
- Forte couplage entre `Jeu`, `Personnage`, `Deplacement` et `Donjon`

## Autres Points Importants

### Architecture
- Absence de pattern Repository pour la gestion des données
- Pas de séparation claire entre la couche présentation et la logique métier
- Manque d'utilisation de l'injection de dépendances

### Sécurité
- Pas de validation des entrées utilisateur pour les commandes de jeu
