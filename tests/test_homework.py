"""Тесты к заданиям после первой лекции.

Для запуска введите команду `pytest -s -v tests/test_homework.py`
"""

from homework_1 import bananas, count_find_num, domain_name, int32_to_ip, zeros

import pytest


# @pytest.mark.skip('[ISSUE-23414] Issue with network connection')
class TestHomework:
    """Тест для задач."""

    # @pytest.mark.skip('test_homework_1_01 ')
    def test_homework_1_01(self):
        """Тест к задаче №1."""
        assert domain_name("http://google.com") == "google"
        assert domain_name("http://google.co.jp") == "google"
        assert domain_name("www.xakep.ru") == "xakep"
        assert domain_name("https://youtube.com") == "youtube"

    @pytest.mark.skip('test_homework_1_02')
    def test_homework_1_02(self):
        """Тест к задаче №2."""
        assert int32_to_ip(2154959208) == "128.114.17.104"
        assert int32_to_ip(0) == "0.0.0.0"
        assert int32_to_ip(2149583361) == "128.32.10.1"

    @pytest.mark.skip('test_homework_1_03')
    def test_homework_1_03(self):
        """Тест к задаче №3."""
        assert zeros(0) == 0
        assert zeros(6) == 1
        assert zeros(30) == 7

    @pytest.mark.skip('test_homework_1_04')
    def test_homework_1_04(self):
        """Тест к задаче №4."""
        assert bananas("banann") == set()
        assert bananas("banana") == {"banana"}
        assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                        "b-a--nana", "-banan--a", "b-ana--na",
                                        "b---anana", "-bana--na", "-ba--nana",
                                        "b-anan--a", "-ban--ana", "b-anana--"}
        assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
        assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",
                                       "b--anana", "banana--", "banan--a"}

    @pytest.mark.skip('test_homework_1_05')
    @pytest.mark.parametrize('primesL, limit, result', [
        ([2, 3], 200, [13, 192]),
        ([2, 5], 200, [8, 200]),
        ([2, 3, 5], 500, [12, 480]),
        ([2, 3, 5], 1000, [19, 960]),
        ([2, 3, 47], 200, [])
        ])
    def test_homework_1_05(self, primesL, limit, result):
        """Тест к задаче №5."""
        assert count_find_num(primesL, limit) == result
