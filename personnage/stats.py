from dataclasses import dataclass

@dataclass(frozen=True)
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
