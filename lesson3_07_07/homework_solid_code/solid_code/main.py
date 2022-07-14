"""Код, который спасет мир."""
from heroes import ChackNorris, SuperHero, Superman

from newscreator import NewsCreater, NewsPaper, PlanetMedia, TVShows

from places import Town, Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Town, news: NewsCreater):
    hero.inspect(place)
    hero.attack()
    news.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPaper())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), PlanetMedia())
    print('-' * 20)
    save_the_place(Superman(), Tokyo(), TVShows())
