from unittest import TestCase

from util import pad_array, array_neighbors


class TestUtil(TestCase):
    def test_pad_array_length(self):
        arr = [[1, 2, 3], "ab", (4, 5, "six")]

        p_arr = pad_array(arr, padding=0)

        self.assertEqual(5, len(p_arr))
        for i in range(5):
            self.assertEqual(5, len(p_arr[i]))

    def test_pad_array_values(self):
        arr = [[1, 2, 3], "ab", (4, 5, "six")]

        p_arr = pad_array(arr, padding=0)

        self.assertEqual(1, p_arr[1][1])
        self.assertEqual("six", p_arr[3][3])
        self.assertEqual(0, p_arr[2][3])

    def test_array_neighbors_values(self):
        arr = [
            list(r)
            for r in [
                "abc---",
                "d.e---",
                "fgh---",
                "-1234-",
                "-5..6-",
                "-7890-",
            ]
        ]
        self.assertEqual(list("1234567890"), array_neighbors(arr, (4, 2), 2))
        self.assertEqual(list("abcdefgh"), array_neighbors(arr, (1, 1)))

    def test_array_neigbors_boundaries(self):
        arr = [
            list(r)
            for r in [
                "------",
                "------",
                "------",
                "------",
                "------",
                "------",
            ]
        ]
        with self.assertRaises(IndexError):
            array_neighbors(arr, (1, 1), span=5)

        for boundary_pos in [(0, 3), (2, 0), (5, 4), (2, 5)]:
            with self.assertRaises(IndexError):
                array_neighbors(arr, boundary_pos)
