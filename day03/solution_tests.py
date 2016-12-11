import unittest

from day03.solution import count_possible_triangles


class SolutionPartOneTests(unittest.TestCase):

    def test_valid(self):
        triangles_input = '2 3 4'
        result = count_possible_triangles(triangles_input)
        self.assertEqual(1, result)

    def test_common_pythagorean_triples(self):
        triangles_input = '3	4	5\n' \
                          '5	12	13\n' \
                          '8	15	17\n' \
                          '7	24	25\n' \
                          '9	40	41\n'
        result = count_possible_triangles(triangles_input)
        self.assertEqual(5, result)

    def test_example_invalid(self):
        triangles_input = '5 10 25'
        result = count_possible_triangles(triangles_input)
        self.assertEqual(0, result)
