"""Несоблюден: Принцип подстановки Барбары Лисков.

Проблема: Сигнатура метода изменилась. 
Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой.
По SOLID: Не допускать таких вольностей.
Когда возникнут трудности? При первой же битве.
"""

from antagonistfinder import AntagonistFinder

from superheroweapon import ChackNorrisWeapon, SuperManWeapon


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.inspector = AntagonistFinder()

    def inspect(self, place):
        self.inspector.get_antagonist(place)

    def attack(self):
        pass

    def ultimate(self):
        pass


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)
        self.weapon = SuperManWeapon()

    def attack(self):
        self.weapon.roundhouse_kick()

    def ultimate(self):
        self.weapon.incinerate_with_lasers()


class ChackNorris(SuperHero):

    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)
        self.weapon = ChackNorrisWeapon()

    def attack(self):
        self.weapon.fire_a_gun()
        self.weapon.roundhouse_kick()
