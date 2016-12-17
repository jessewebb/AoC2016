import unittest

from day04.solution import Room, calculate_sum_of_real_room_sector_ids


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


class CalculateSumOfRealRoomSectorIdsTests(unittest.TestCase):

    def test_example(self):
        list_of_rooms_as_text = 'aaaaa-bbb-z-y-x-123[abxyz]\n' \
                                'a-b-c-d-e-f-g-h-987[abcde]\n' \
                                'not-a-real-room-404[oarel]\n' \
                                'totally-real-room-200[decoy]\n'
        expected_sum_of_real_room_sector_ids = 1514
        result = calculate_sum_of_real_room_sector_ids(list_of_rooms_as_text)
        self.assertEqual(result, expected_sum_of_real_room_sector_ids)
