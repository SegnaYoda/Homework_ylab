"""Циклический итератор.

Итератор итеририруется по итерируемому объекту (list, tuple, set, range,
Range2, и т. д.), по достижению последнего элемента, начинает сначала.
"""
import itertools
import time


class CyclicIterator:
    """Циклический итератор."""

    def __init__(self, content):
        """Инцициализация итерируемого объекта."""
        self.content = itertools.cycle(content)

    def __iter__(self):
        """Возвращает объект итератора."""
        return self

    def __next__(self):
        """Переход к следующему значению объекта итератора."""
        time.sleep(0.2)  # для более удобного чтения вывода с консоли
        return next(self.content)


class Range2:
    """Класс необходим для проверки условия задания."""

    def __init__(self, stop_value: int):
        """Инцициализация."""
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        """Возвращает объект итератора."""
        return self

    def __next__(self):
        """Переход к следующему значению объекта итератора."""
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration


a = [(0, 1), (4, 1), (7, 2), (5, 5), (1, 4), (10, 2)]
b = (123, "123", "aasa", 900002)
c = {123, "123", "aasa", 900002}
rit = "123ABC"
dict1 = {123: "FIGD", "BBC": 900002, (42,): [1, 2, 3]}
range1 = range(3)
range2 = Range2(5)

cyclic_iterator = CyclicIterator(dict1)

if __name__ == "__main__":
    for i in cyclic_iterator:
        print(i)
