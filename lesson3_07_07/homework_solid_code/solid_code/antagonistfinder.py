"""Несоблюден: Принцип инверсии зависимостей.

Проблема: Класс, отвечающий за вызов верного метода у классов разного типа добавляет излишнюю сложность.
По SOLID: Создать абстрактный класс Place, обязывающий реализовать метод для поиска злодея.
Когда возникнут трудности: Когда ваш проект обретет мировую славу.
"""


class AntagonistContaingPlace:
    """Абстрактный класс Place по заданию."""

    def get_antagonist(self):
        pass


class AntagonistFinder:

    def get_antagonist(self, place: AntagonistContaingPlace):
        place.get_antagonist()
