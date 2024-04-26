import os
from unittest import TestCase

from config import days
from solution import Game, solution


class TestSolution(TestCase):

    def setUp(self):
        with open(os.path.join(days[1], "test_input")) as f:
            self.input = f.read()

    def test_parse_methods(self):
        lines = self.input.splitlines()
        games = [Game.parse(test_line) for test_line in lines]
        print(games)
        # i just looked at em ;)
        self.assertEqual(5, len(games))

    def test_solution(self):
        self.assertEqual(8, solution(self.input))
        self.assertEqual(2286, solution(self.input, part=2))

    def test_game_min_set(self):
        lines = self.input.splitlines()
        games = [Game.parse(test_line) for test_line in lines]

        for i, test_case in enumerate(
            [
                [4, 2, 6],
                [1, 3, 4],
                [20, 13, 6],
                [14, 3, 15],
                [6, 3, 2],
            ]
        ):
            with self.subTest(""):
                self.assertEqual(test_case, games[i].min_set())

    def test_game_power(self):
        lines = self.input.splitlines()
        games = [Game.parse(test_line) for test_line in lines]

        for i, test_case in enumerate([48, 12, 1560, 630, 36]):
            with self.subTest(""):
                self.assertEqual(test_case, games[i].power())
