from abc import ABC, abstractmethod

class ClasseProvider(ABC):
    @property
    @abstractmethod
    def nom(self):
        pass

    @property
    @abstractmethod
    def stats(self):
        pass

class MonstreProvider(ABC):
    @property
    @abstractmethod
    def nom(self):
        pass

    @property
    @abstractmethod
    def stats(self):
        pass
