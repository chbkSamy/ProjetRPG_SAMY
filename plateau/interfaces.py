from typing import Protocol
from abc import ABC, abstractmethod
class Positionnable(Protocol):
    @property
    def position(self) -> tuple[int, int]: ...

    def deplacer(self, x: int, y: int) -> None: ...


class IJoueur(ABC):
    @abstractmethod
    def tourner(self, direction: str) -> str: ...

    @abstractmethod
    def get_position(self) -> tuple[int, int]: ...

    @abstractmethod
    def get_orientation(self) -> str: ...
