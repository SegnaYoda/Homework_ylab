"""Задачи после первой лекций.

Реализованы тесты через библиотеку Pytest.
"""

import re
from functools import reduce
from operator import mul


def domain_name(url):
    """Задача №1.

    Метод domain_name, который возвращает домен из url адреса.
    """
    pattern = r"(.*?\/\/)?(www\.)?([^\.]*)"
    result = re.match(pattern, url)
    return result.group(3)


def int32_to_ip(int32):
    """Задача №2.

    Метод int32_to_ip, кот. принимает на вход 32-битное целое
    число (integer) и возвращает строковое представление
    его в виде IPv4-адреса.

    *В этом способе решения проверять является ли число 64-битным
    нет необходимости.
    """
    ip_1 = (int32 >> 24) & (2**8 - 1)
    ip_2 = (int32 >> 16) & (2**8 - 1)
    ip_3 = (int32 >> 8) & (2**8 - 1)
    ip_4 = int32 & (2**8 - 1)
    result = str(ip_1) + '.' + str(ip_2) + '.' + str(ip_3) + '.' + str(ip_4)
    return result


def zeros(n):
    """Задача №3.

    Метод zeros, который принимает на вход целое число (integer)
    и возвращает количество конечных нулей в факториале
    (N! = 1 * 2 * 3 * ... * N) заданного числа.
    """
    result = 0
    while n // 5 > 0:
        result += n // 5
        n = n // 5
    return result


def bananas(s):
    """Задача №4.

    Метод bananas, который принимает на вход строку
    и возвращае  т количество слов «banana» в строке.
    """
    banana = "banana"
    graph_number = len(s) - len(banana)
    result = set()
    input_word = list(s)

    def dfs(input_word, graph_number, j=0, ii=0):
        """Метод c рекурсией."""
        for i in range(ii, len(input_word) - (graph_number - j)):
            temporary = input_word[i]
            input_word[i] = "-"
            if j < graph_number:
                dfs(input_word, graph_number, j+1, i+1)
            else:
                if "".join(input_word).replace("-", "") == banana:
                    result.add("".join(input_word))
            input_word[i] = temporary
        return result
    if s == banana:
        return {s}
    elif graph_number == 0:
        return set()
    else:
        return dfs(input_word, graph_number-1)


def count_find_num(primesL, limit):
    """Задача №5.

    Метод count_find_num, который принимает на вход список простых
    множителей (primesL) и целое число, предел (limit), после чего
    попробуйте сгенерировать по порядку все числа.
    Меньшие значения предела, которые имеют все и только простые
    множители простых чисел primesL.
    """
    def dfs(primesL, limit, result, current_number):
        """Метод поиска в глубину."""
        for i in range(len(primesL)):
            if current_number * primesL[i] <= limit:
                result.add(current_number * primesL[i])
                dfs(primesL, limit, result, current_number * primesL[i])
        return [len(result), max(result)]
    # получаем произведение элементов списка
    current_number = reduce(mul, primesL)
    if current_number <= limit:
        return dfs(primesL, limit, {current_number}, current_number)
    return []
