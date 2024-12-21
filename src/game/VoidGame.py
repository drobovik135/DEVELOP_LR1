from abc import ABC, abstractmethod


class VoidGame(ABC):
    def __init__(self):
        self.answer = None

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def printer(self):
        pass

    def checkAnswer(self, inputer):
        if str(self.answer) == inputer:
            print("You are right")
        else:
            print("You lose")

    def start(self):
        self.generate()
        self.printer()
        inputer = input("Your answer: ")
        self.checkAnswer(inputer)

