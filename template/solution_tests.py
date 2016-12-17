import unittest

from template.solution import foo


class SolutionPartOneTests(unittest.TestCase):

    def test_foo(self):
        with self.assertRaises(NotImplementedError):
            foo('bar')
