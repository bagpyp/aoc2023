import os
from unittest import TestCase

from config import days
from solution import solution


class TestSolution(TestCase):

    def setUp(self):
        with open(os.path.join(days[0], "test_input")) as f:
            self.input = f.read()

    def test_solution(self):
        self.assertEqual(0, solution(self.input))
        self.assertEqual(0, solution(self.input, part=2))
