import unittest

from day04.solution import Room, calculate_sum_of_real_room_sector_ids, find_sector_id_of_real_room


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


class RoomNameTests(unittest.TestCase):

    def test_roll_a_by_1_to_b(self):
        room = Room('a', 1, 'test')
        self.assertEqual('b', room.name)

    def test_roll_b_by_1_to_c(self):
        room = Room('b', 1, 'test')
        self.assertEqual('c', room.name)

    def test_roll_z_by_1_to_a(self):
        room = Room('z', 1, 'test')
        self.assertEqual('a', room.name)

    def test_roll_a_by_25_to_z(self):
        room = Room('a', 25, 'test')
        self.assertEqual('z', room.name)

    def test_roll_a_by_26_to_a(self):
        room = Room('a', 26, 'test')
        self.assertEqual('a', room.name)

    def test_roll_a_by_52_to_a(self):
        room = Room('a', 52, 'test')
        self.assertEqual('a', room.name)

    def test_hyphens_to_spaces(self):
        room = Room('-', 0, 'test')
        self.assertEqual(' ', room.name)

    def test_letters_and_hyphens(self):
        room = Room('abc-def', 79, 'test')  # 79 rolls over 3 times and then adds one letter
        self.assertEqual('bcd efg', room.name)

    def test_example(self):
        room = Room('qzmt-zixmtkozy-ivhz', 343, 'test')
        self.assertEqual('very encrypted name', room.name)


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


class FindSectorIdOfRealRoomTests(unittest.TestCase):

    def test_only_entry_in_list_decrypted(self):
        list_of_rooms_as_text = 'abc-def-0[abcde]\n'
        result = find_sector_id_of_real_room(list_of_rooms_as_text, 'abc def')
        self.assertEqual(result, 0)

    def test_only_entry_in_list_encrypted(self):
        list_of_rooms_as_text = 'zab-cde-53[abcde]\n'
        result = find_sector_id_of_real_room(list_of_rooms_as_text, 'abc def')
        self.assertEqual(result, 53)

    def test_not_in_the_list(self):
        list_of_rooms_as_text = 'abc-def-0[abcde]\n'
        result = find_sector_id_of_real_room(list_of_rooms_as_text, 'not in the list')
        self.assertIsNone(result)

    def test_northpole_in_between_example_rooms_from_part_one(self):
        list_of_rooms_as_text = 'aaaaa-bbb-z-y-x-123[abxyz]\n' \
                                'a-b-c-d-e-f-g-h-987[abcde]\n' \
                                'northpole-object-storage-260[oetra]\n' \
                                'not-a-real-room-404[oarel]\n' \
                                'totally-real-room-200[decoy]\n'
        result = find_sector_id_of_real_room(list_of_rooms_as_text, 'northpole object storage')
        self.assertEqual(result, 260)

