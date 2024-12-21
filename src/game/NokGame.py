from .VoidGame import VoidGame
import math
import random
from functools import reduce


class NokGame(VoidGame):
    def __init__(self):
        super().__init__()
        self.answer = -1
        self.quest = ""

    def generate(self):
        numbers = []
        n = 3
        for i in range(n):
            numbers.append(random.randint(2, 15))

        self.answer = reduce(math.lcm, numbers)
        for i in numbers:
            self.quest += str(i) + " "

    def printer(self):
        print("Find the smallest common multiple of given numbers")
        print(self.quest)
