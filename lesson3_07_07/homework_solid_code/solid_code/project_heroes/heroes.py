"""Несоблюден: Принцип подстановки Барбары Лисков.

Проблема: Сигнатура метода изменилась.
Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой.
По SOLID: Не допускать таких вольностей.
Когда возникнут трудности? При первой же битве.
"""
from project_heroes.antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name):
        self.inspector = AntagonistFinder()
        self.name = name

    def inspect(self, place):
        self.inspector.get_antagonist(place)

    def attack(self):
        pass
