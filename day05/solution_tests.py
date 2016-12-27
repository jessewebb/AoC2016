import unittest

from day05.solution import generate_password, generate_password2


class SolutionPartOneTests(unittest.TestCase):

    def test_example(self):
        door_id = 'abc'

        password = generate_password(door_id, 8)
        self.assertEqual(password, '18f47a30')


class SolutionPartTwoTests(unittest.TestCase):

    def test_example(self):
        door_id = 'abc'

        password = generate_password2(door_id, 8)
        self.assertEqual(password, '05ace8e3')
