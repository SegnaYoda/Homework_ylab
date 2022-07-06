"""Тесты к заданиям после первой лекции.

Для запуска введите команду `pytest -s -v tests/test_homework.py`
"""

from homework_1 import bananas, count_find_num, domain_name, int32_to_ip, zeros

import pytest


@pytest.mark.skip('Тесты для решений задач после первой лекции.')
class TestHomework_1:
    """Тест для задач."""

    # @pytest.mark.skip('homework_1_01')
    def test_homework_1_01(self):
        """Тест к задаче №1."""
        assert domain_name("http://google.com") == "google"
        assert domain_name("http://google.co.jp") == "google"
        assert domain_name("www.xakep.ru") == "xakep"
        assert domain_name("https://youtube.com") == "youtube"
        assert domain_name("http://github.com/carbonfive/raygun") == "github"
        assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
        assert domain_name("https://www.cnet.com") == "cnet"
        assert domain_name("cnet.com") == "cnet"

    # @pytest.mark.skip('homework_1_02')
    def test_homework_1_02(self):
        """Тест к задаче №2."""
        assert int32_to_ip(2154959208) == "128.114.17.104"
        assert int32_to_ip(0) == "0.0.0.0"
        assert int32_to_ip(2149583361) == "128.32.10.1"
        assert int32_to_ip(32) == "0.0.0.32"

    # @pytest.mark.skip('homework_1_03')
    def test_homework_1_03(self):
        """Тест к задаче №3."""
        assert zeros(0) == 0
        assert zeros(6) == 1
        assert zeros(30) == 7
        assert zeros(12) == 2

    # @pytest.mark.skip('homework_1_04')
    @pytest.mark.parametrize('input_data, result_data', [
        ("banann", set()),
        ("banana", {"banana"}),
        ("bbananana", {"b-an--ana", "-banana--", "-b--anana",
                       "b-a--nana", "-banan--a", "b-ana--na",
                       "b---anana", "-bana--na", "-ba--nana",
                       "b-anan--a", "-ban--ana", "b-anana--"}),
        ("bananaaa", {"banan-a-", "banana--", "banan--a"}),
        ("bananana", {"ban--ana", "ba--nana", "bana--na",
                      "b--anana", "banana--", "banan--a"})])
    def test_homework_1_04(self, input_data, result_data):
        """Тест к задаче №4."""
        assert bananas(input_data) == set(result_data)

    # @pytest.mark.skip('homework_1_05')
    @pytest.mark.parametrize('primesL, limit, result', [
        ([2, 3], 200, [13, 192]),
        ([2, 5], 200, [8, 200]),
        ([2, 3, 5], 500, [12, 480]),
        ([2, 3, 5], 1000, [19, 960]),
        ([2, 3, 47], 200, []),
        ])
    def test_homework_1_05(self, primesL, limit, result):
        """Тест к задаче №5."""
        self.primesL = primesL
        self.limit = limit
        self.result = result
        assert count_find_num(self.primesL, self.limit) == self.result


@pytest.mark.skip('Тесты для решений задач после второй лекции.')
class TestHomework_2:
    """Тест для задач после второй лекции."""

    def test_homework_2(self, input_data):
        """Тест к задаче №4."""
        assert function_homework2(input_data) == "(0, 1) -> (1, 4)[3.1622776601683795] -> (4, 1)[7.404918347287664] -> (5, 5)[11.528023972905324] -> (7, 2)[15.133575248369313] -> (0, 1)[22.204643060234787] = 22.204643060234787"