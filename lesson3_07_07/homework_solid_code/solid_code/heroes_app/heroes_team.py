from heroes_app.heropower import ChackNorrisWeapon, SuperManWeapon

from project_heroes.heroes import SuperHero


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
        self.weapon.roundhouse_kick()
