"""Несоблюден: Принцип подстановки Барбары Лисков.

Проблема: Сигнатура метода изменилась.
Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой.
По SOLID: Не допускать таких вольностей.
Когда возникнут трудности? При первой же битве.
"""
from abc import ABC, abstractmethod

from project_heroes.antagonistfinder import AntagonistFinder


class SuperHero(ABC):

    def __init__(self, name):
        self.inspector = AntagonistFinder()
        self.name = name

    def inspect(self, place):
        self.inspector.get_antagonist(place)

    @abstractmethod
    def attack(self):
        pass
