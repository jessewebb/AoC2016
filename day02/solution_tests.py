import unittest

from solution import calculate_keypad_code


class SolutionTests(unittest.TestCase):

    # part one

    def test_one_move_up(self):
        instructions = 'U'
        result = calculate_keypad_code(instructions)
        self.assertEqual('2', result)

    def test_one_move_right(self):
        instructions = 'R'
        result = calculate_keypad_code(instructions)
        self.assertEqual('6', result)

    def test_one_move_down(self):
        instructions = 'D'
        result = calculate_keypad_code(instructions)
        self.assertEqual('8', result)

    def test_one_move_left(self):
        instructions = 'L'
        result = calculate_keypad_code(instructions)
        self.assertEqual('4', result)

    def test_two_moves_up(self):
        instructions = 'UU'
        result = calculate_keypad_code(instructions)
        self.assertEqual('2', result)

    def test_two_moves_right(self):
        instructions = 'RR'
        result = calculate_keypad_code(instructions)
        self.assertEqual('6', result)

    def test_two_moves_down(self):
        instructions = 'DD'
        result = calculate_keypad_code(instructions)
        self.assertEqual('8', result)

    def test_two_moves_left(self):
        instructions = 'LL'
        result = calculate_keypad_code(instructions)
        self.assertEqual('4', result)

    def test_four_moves_in_a_circle(self):
        instructions = 'URDL'
        result = calculate_keypad_code(instructions)
        self.assertEqual('5', result)

    def test_eight_moves_in_a_circle(self):
        instructions = 'UURRDDLL'
        result = calculate_keypad_code(instructions)
        self.assertEqual('7', result)

    def test_two_lines_of_instructions_with_same_starting_point(self):
        instructions = 'URDL\nLLUURRDD'
        result = calculate_keypad_code(instructions)
        self.assertEqual('59', result)

    def test_two_lines_of_instructions_with_different_starting_points(self):
        instructions = 'RDLUULD\nRRRUDDDLUUU'
        result = calculate_keypad_code(instructions)
        self.assertEqual('42', result)

    def test_example(self):
        instructions = 'ULL\nRRDDD\nLURDL\nUUUUD'
        result = calculate_keypad_code(instructions)
        self.assertEqual('1985', result)
