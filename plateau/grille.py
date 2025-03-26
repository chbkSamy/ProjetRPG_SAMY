from typing import Dict, Optional

class Grille:
    def __init__(self, largeur: int = 5, hauteur: int = 5):
        self._largeur = largeur
        self._hauteur = hauteur
        self._monstres: Dict[tuple[int, int], object] = {}
        self._tresors: Dict[tuple[int, int], str] = {}
        self._obstacles: Dict[tuple[int, int], bool] = {}

    def valider_position(self, x: int, y: int) -> bool:
        return 0 <= x < self._largeur and 0 <= y < self._hauteur

    def ajouter_monstre(self, x: int, y: int, monstre: object) -> None:
        if not self.valider_position(x, y):
            raise ValueError("Position invalide")
        self._monstres[(x, y)] = monstre

    def obtenir_monstre(self, x: int, y: int) -> Optional[object]:
        return self._monstres.get((x, y))

    def ajouter_tresor(self, x: int, y: int, tresor: str) -> None:
        if not self.valider_position(x, y):
            raise ValueError("Position invalide")
        self._tresors[(x, y)] = tresor

    def obtenir_tresor(self, x: int, y: int) -> Optional[str]:
        return self._tresors.get((x, y))

    def ajouter_obstacle(self, x: int, y: int) -> None:
        if not self.valider_position(x, y):
            raise ValueError("Position invalide")
        self._obstacles[(x, y)] = True

    def obtenir_obstacle(self, x: int, y: int) -> Optional[bool]:
        return self._obstacles.get((x, y))

    def generer_monstres_aleatoires(self, monstres_disponibles: list, nombre: int) -> None:
        import random
        for _ in range(nombre):
            x = random.randint(0, self._largeur - 1)
            y = random.randint(0, self._hauteur - 1)
            self.ajouter_monstre(x, y, random.choice(monstres_disponibles))
