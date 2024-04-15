from unittest import TestCase

from solution import solution


class TestSolution(TestCase):

    def setUp(self):
        with open("1-trebuchet/test_input") as f:
            self.test_input = f.read()

    def test_solution(self):
        self.assertEqual(142, solution(self.test_input))
