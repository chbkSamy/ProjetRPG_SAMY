from dataclasses import dataclass
from typing import Protocol

@dataclass
class Stats:
    pv: int
    pm: int
    force: int
    intelligence: int
    defense: int
    resistance_magique: int
    agilite: int
    chance: int
    endurance: int
    esprit: int

class ClasseProvider(Protocol):
    @property
    def nom(self) -> str: ...

    @property
    def stats(self) -> Stats: ...

class MonstreProvider(Protocol):
    @property
    def nom(self) -> str: ...

    @property
    def stats(self) -> Stats: ...
