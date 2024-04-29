import os
from unittest import TestCase

from config import days
from solution import solution
from util import get_day


class TestSolution(TestCase):

    def setUp(self):
        with open(os.path.join(days[get_day(__file__)], "test_input")) as f:
            self.input = f.read()

    def test_solution(self):
        self.assertEqual(4361, solution(self.input))
        self.assertEqual(467835, solution(self.input, part=2))
