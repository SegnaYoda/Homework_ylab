"""Задачи после первой лекций.

Реализованы тесты через библиотеку Pytest.
"""

import re


def domain_name(url):
    """Задача №1.

    Метод domain_name, который возвращает домен из url адреса.
    """
    pattern = r"(?:(.*?\/\/?w{3}.)|(.*?\/\/)|(^w{3}.))([^\.]*)"
    result = re.match(pattern, url)
    return result.group(4)


def int32_to_ip(int32):
    """Задача №2.

    Метод int32_to_ip, кот. принимает на вход 32-битное целое
    число (integer) и возвращает строковое представление
    его в виде IPv4-адреса.
    """
    # return
    pass


def zeros(n):
    """Задача №3.

    Метод zeros, который принимает на вход целое число (integer)
    и возвращает количество конечных нулей в факториале
    (N! = 1 * 2 * 3 * ... * N) заданного числа.
    """
    # return 0
    pass


def bananas(s) -> set:
    """Задача №4.

    Метод bananas, который принимает на вход строку
    и возвращает количество слов «banana» в строке.
    """
    # result = set()
    # return result
    pass


def count_find_num(primesL, limit):
    """Задача №5.

    Метод count_find_num, который принимает на вход список простых
    множителей (primesL) и целое число, предел (limit), после чего
    попробуйте сгенерировать по порядку все числа.
    Меньшие значения предела, которые имеют все и только простые
    множители простых чисел primesL.
    """
    # return []
    pass
