from project_heroes.places import Town


class Kostroma(Town):

    def __init__(self):
        super(Kostroma, self).__init__("Kostroma", (57.7665, 40.9269))

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Town):

    def __init__(self):
        super(Tokyo, self).__init__("Tokyo", (35.6895, 139.692))

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
