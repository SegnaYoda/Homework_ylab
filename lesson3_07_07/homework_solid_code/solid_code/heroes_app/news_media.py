from project_heroes.newscreator import NewsCreater


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
        place_crdnts = getattr(place, 'coordinates')
        hero_name = getattr(hero, 'name')
        print(f'{hero_name} saved the {place_crdnts}!')