import os
from unittest import TestCase

from config import days
from solution import solution, parse_input
from util import get_day


class TestSolution(TestCase):

    def setUp(self):
        with open(os.path.join(days[get_day(__file__)], "test_input")) as f:
            self.input = f.read()

    def test_parse_input(self):
        data = parse_input(self.input)

        self.assertEqual(data.get("seeds")[0], 79)
        self.assertEqual(data.get("soil-to-fertilizer")[0].get("source-start"), 15)
        self.assertEqual(data.get("soil-to-fertilizer")[0].get("range-length"), 37)
        self.assertEqual(len(data), 8)

    def test_solution(self):
        self.assertEqual(0, solution(self.input))
        self.assertEqual(0, solution(self.input, part=2))
