from abc import ABC, abstractmethod

class Lobby(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def body(self):
        pass