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


class SolutionPartTwoTests(unittest.TestCase):

    def test_three_possible_triangle(self):
        triangles_input = '3  5  8\n' \
                          '4 12 15\n' \
                          '5 13 17\n'
        result = count_possible_triangles(triangles_input, vertically=True)
        self.assertEqual(3, result)

    def test_example_input(self):
        triangles_input = '101 301 501\n' \
                          '102 302 502\n' \
                          '103 303 503\n' \
                          '201 401 601\n' \
                          '202 402 602\n' \
                          '203 403 603\n'
        result = count_possible_triangles(triangles_input, vertically=True)
        self.assertEqual(6, result)
