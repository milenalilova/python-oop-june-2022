from project.dark_knight import DarkKnight
from project.elf import Elf
from project.hero import Hero


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)
