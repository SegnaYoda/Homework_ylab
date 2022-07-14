"""Несоблюден: Принцип подстановки Барбары Лисков.

Проблема: Сигнатура метода изменилась.
Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой.
По SOLID: Не допускать таких вольностей.
Когда возникнут трудности? При первой же битве.
"""

from antagonistfinder import AntagonistFinder

from superheroweapon import ChackNorrisWeapon, SuperManWeapon


class SuperHero:

    def __init__(self, name):
        self.inspector = AntagonistFinder()
        self.name = name

    def inspect(self, place):
        self.inspector.get_antagonist(place)

    def attack(self):
        pass


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent')
        self.weapon = SuperManWeapon()

    def attack(self):
        self.weapon.roundhouse_kick()
        self.ultimate()

    def ultimate(self):
        self.weapon.incinerate_with_lasers()


class ChackNorris(SuperHero):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris')
        self.weapon = ChackNorrisWeapon()

    def attack(self):
        self.weapon.fire_a_gun()
