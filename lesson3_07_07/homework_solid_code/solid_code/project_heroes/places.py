"""Сущности городов."""
from project_heroes.antagonistfinder import AntagonistContaingPlace


class Town(AntagonistContaingPlace):

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
