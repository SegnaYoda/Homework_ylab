"""Код, который спасет мир."""


from typing import Union

from heroes import ChackNorris, SuperHero, Superman

from newscreator import NewsPaper, PlanetMedia, TVShows

from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], news: Union[NewsPaper, TVShows, PlanetMedia]):
    hero.inspect(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPaper())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), PlanetMedia())
    print('-' * 20)
    save_the_place(Superman(), Tokyo(), TVShows())
