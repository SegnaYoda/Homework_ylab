"""Код, который спасет мир."""
from heroes_app.heroes_team import ChackNorris, Superman
from heroes_app.news_media import NewsPaper, PlanetMedia, TVShows
from heroes_app.towns import Kostroma, Tokyo

from project_heroes.heroes import SuperHero
from project_heroes.newscreator import NewsCreater
from project_heroes.places import Town


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
