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


class RoomFromInputLineTests(unittest.TestCase):

    def test_example1(self):
        room_input_line = 'aaaaa-bbb-z-y-x-123[abxyz]'
        expected_room = Room('aaaaa-bbb-z-y-x', 123, 'abxyz')
        result = Room.from_input_line(room_input_line)
        self.assertEqual(result, expected_room)

    def test_example2(self):
        room_input_line = 'a-b-c-d-e-f-g-h-987[abcde]'
        expected_room = Room('a-b-c-d-e-f-g-h', 987, 'abcde')
        result = Room.from_input_line(room_input_line)
        self.assertEqual(result, expected_room)

    def test_example3(self):
        room_input_line = 'not-a-real-room-404[oarel]'
        expected_room = Room('not-a-real-room', 404, 'oarel')
        result = Room.from_input_line(room_input_line)
        self.assertEqual(result, expected_room)

    def test_example4(self):
        room_input_line = 'totally-real-room-200[decoy]'
        expected_room = Room('totally-real-room', 200, 'decoy')
        result = Room.from_input_line(room_input_line)
        self.assertEqual(result, expected_room)

