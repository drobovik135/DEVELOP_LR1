from typing import Type

from .Lobby import Lobby
from ..game.NokGame import NokGame
from ..game.ProgressionGame import ProgressionGame
from ..game.VoidGame import VoidGame


class SimpleLobby(Lobby):
    def __init__(self):
        self.name = ""
        self.scan = None

    def selector(self, i: int):
        if i == 1:
            return NokGame()
        elif i == 2:
            return ProgressionGame()
        elif i == 3:
            exit(0)
        return None

    def game_select(self):
        print("Pick the game: 1 - NokGame; 2 - ProgressionGame; 3 - Exit")

        select = int(input())
        game = self.selector(select)
        game.start()

    def start(self):
        print("Welcome to the Brain Games! May I have your name?")
        self.name = input()
        print(f"Hello, {self.name}!")
        self.body()

    def body(self):
        while True:
            self.game_select()
