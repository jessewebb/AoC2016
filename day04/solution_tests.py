import unittest

from day04.solution import Room


class RoomIsRealTests(unittest.TestCase):

    def test_example1(self):
        room = Room('aaaaa-bbb-z-y-x', 123, 'abxyz')
        self.assertTrue(room.is_real)

    def test_example2(self):
        room = Room('a-b-c-d-e-f-g-h', 987, 'abcde')
        self.assertTrue(room.is_real)

    def test_example3(self):
        room = Room('not-a-real-room', 404, 'oarel')
        self.assertTrue(room.is_real)

    def test_example4(self):
        room = Room('totally-real-room', 200, 'decoy')
        self.assertFalse(room.is_real)
