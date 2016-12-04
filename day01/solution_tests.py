import unittest

from day01.solution import calculate_shortest_grid_distance


class SolutionTests(unittest.TestCase):

    # part one

    def test_one_right_turn(self):
        instructions = 'R1'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(1, result)

    def test_one_left_turn(self):
        instructions = 'L2'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(2, result)

    def test_two_right_turns(self):
        instructions = 'R1, R2'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(3, result)

    def test_two_left_turns(self):
        instructions = 'L3, L4'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(7, result)

    def test_many_right_turns(self):
        instructions = 'R1, R2, R3, R4, R5'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(5, result)

    def test_many_left_turns(self):
        instructions = 'L2, L3, L4, L5, L10'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(10, result)

    def test_example1(self):
        instructions = 'R2, L3'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(5, result)

    def test_example2(self):
        instructions = 'R2, R2, R2'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(2, result)

    def test_example3(self):
        instructions = 'R5, L5, R5, R3'
        result = calculate_shortest_grid_distance(instructions)
        self.assertEqual(12, result)

    # part two

    def test_stop_at_first_location_visited_twice_example(self):
        instructions = 'R8, R4, R4, R8'
        result = calculate_shortest_grid_distance(instructions, stop_at_first_location_visited_twice=True)
        self.assertEqual(4, result)
