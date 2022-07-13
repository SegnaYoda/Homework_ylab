"""Несоблюден: Принцип единой ответственности.

Проблема: Герой не должен заниматься оповещениями о своей победе, это задача масс-медиа.
По SOLID: Вынести оповещение в отдельный класс, занимающийся выводом информации.
Когда возникнут трудности? Добавьте оповещение о победе героя через газеты или через TV (на выбор)
а также попробуйте оповестить планеты (у которых вместа атрибута name:str используется coordinates:List[float]).
"""


class News:

    def create_news(self):
        pass


class NewsCreater:

    news = News()

    def create_news(self):
        pass


class NewsPaper(NewsCreater):

    def create_news(self, place, hero):
        place_name = getattr(place, 'name')
        hero_name = getattr(hero, 'name')
        print(f'{hero_name} saved the {place_name}!')


class TVShows(NewsCreater):

    def create_news(self, place, hero):
        place_name = getattr(place, 'name')
        hero_name = getattr(hero, 'name')
        print(f'{hero_name} saved the {place_name}!')


class PlanetMedia(NewsCreater):

    def create_news(self, place, hero):
        place_name = getattr(place, 'coordinates')
        hero_name = getattr(hero, 'name')
        print(f'{hero_name} saved the {place_name}!')
