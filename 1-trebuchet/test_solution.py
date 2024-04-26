import os
from unittest import TestCase

from config import days
from solution import solution, extract_digits, extract_numbers


class TestSolution(TestCase):

    def setUp(self):
        with open(os.path.join(days[0], "test_input")) as f:
            self.test_input = f.read()
            self.test_lines = self.test_input.splitlines()

    def test_solution(self):
        self.assertEqual(142, solution(self.test_input))

    def test_solution_part_two(self):
        self.assertEqual(
            281,
            solution(
                """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""",
                part=2,
            ),
        )

    def test_extract_digits(self):
        self.assertEqual(["1", "2"], extract_digits("kldsfj1oifjasdoif2dsalfj"))
        self.assertEqual(["1", "1"], extract_digits("kldsfj1oifjasdoifTWOdsalfj"))

    def test_extract_numbers(self):
        test_cases = [
            (["1", "seven"], "abc1defgsevenghi"),
            (["eight", "9"], "eightLSDAKJHASDKJL9kjdff"),
            (["5", "5"], "5c"),
            (["6", "6"], "636"),
        ]
        for expected, test_line in test_cases:
            self.assertEqual(expected, extract_numbers(test_line))
