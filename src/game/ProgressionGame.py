from .VoidGame import VoidGame
import math
import random
from functools import reduce


class ProgressionGame(VoidGame):
    def __init__(self):
        super().__init__()
        self.answer = -1
        self.quest = ""

    def geometric_progression(self, start, ratio, terms):
        progression = [start * (ratio ** i) for i in range(terms)]
        return progression

    def generate(self):
        numbers = self.geometric_progression(
            random.randint(1, 5),
            random.randint(1, 3),
            random.randint(5, 10)
        )
        n = random.randint(0, len(numbers)-1)
        self.answer = numbers[n]
        numbers[n] = ".."

        for num in numbers:
            self.quest += str(num) + " "

    def printer(self):
        print("Find the smallest common multiple of given numbers")
        print(self.quest)
