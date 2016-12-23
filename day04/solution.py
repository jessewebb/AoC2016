
from collections import Counter

import re


class Room(object):

    def __init__(self, encrypted_name, sector_id, checksum):
        self.encrypted_name = encrypted_name
        self.sector_id = sector_id
        self.checksum = checksum

    @property
    def is_real(self):
        return self._perform_checksum()

    def _perform_checksum(self):

        def _compare_letter_counts(x, y):
            x_letter, x_count = x
            y_letter, y_count = y
            if x_count > y_count:  # sort highest counts first
                return -1
            elif x_count < y_count:
                return 1
            else:  # x_count == y_count; break tie by sorting letters alphabetically
                return -1 if x_letter < y_letter else (1 if x_letter > y_letter else 0)

        encrypted_name_letters = [char for char in self.encrypted_name if char.isalpha()]
        letter_counter = Counter(encrypted_name_letters)
        most_common_letters_and_counts = letter_counter.most_common()
        sorted_most_common_letters_and_counts = sorted(most_common_letters_and_counts, cmp=_compare_letter_counts)
        five_most_common_letters = [letter for letter, count in sorted_most_common_letters_and_counts][:5]
        checksum_letters = [letter for letter in self.checksum]
        return five_most_common_letters == checksum_letters

    @property
    def name(self):
        return self._decrypted_name()

    def _decrypted_name(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        char_count = len(chars)
        letter_shift = self.sector_id

        def roll_letter_forward(letter):
            if letter not in chars:
                return letter
            shifted_index = chars.index(letter) + letter_shift % char_count  # shift right
            if shifted_index >= char_count:  # we have passed the end, shift left back into range
                shifted_index -= char_count
            return chars[shifted_index]

        decrypted_name = ''.join(roll_letter_forward(letter) for letter in self.encrypted_name).replace('-', ' ')
        return decrypted_name


    @classmethod
    def from_input_line(cls, room_input_line):
        pattern = r'^(?P<encrypted_name>[a-z-]+)-(?P<sector_id>\d+)\[(?P<checksum>[a-z]{5})\]$'
        match = re.match(pattern, room_input_line)
        return Room(match.group('encrypted_name'),
                    int(match.group('sector_id')),
                    match.group('checksum'))

    def __eq__(self, other):
        return self.encrypted_name == other.encrypted_name and \
               self.sector_id == other.sector_id and \
               self.checksum == other.checksum

    def __repr__(self):
        return '%s(encrypted_name=%r,sector_id=%r,checksum=%r)' % \
               (self.__class__.__name__, self.encrypted_name, self.sector_id, self.checksum)


def _parse_rooms_from_text(list_of_rooms_as_text):
    return [Room.from_input_line(room_input_line) for room_input_line in list_of_rooms_as_text.splitlines()]


def calculate_sum_of_real_room_sector_ids(list_of_rooms_as_text):
    rooms = _parse_rooms_from_text(list_of_rooms_as_text)
    return sum(room.sector_id for room in rooms if room.is_real)


def find_sector_id_of_real_room(list_of_rooms_as_text, room_name):
    rooms = _parse_rooms_from_text(list_of_rooms_as_text)
    real_rooms = (room for room in rooms if room.is_real)
    north_pole_storage_rooms = (room.sector_id for room in real_rooms if room.name == room_name)
    return next(north_pole_storage_rooms, None)


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = calculate_sum_of_real_room_sector_ids(puzzle_input)
    part2_answer = find_sector_id_of_real_room(puzzle_input, 'northpole object storage')
    print 'Part One Answer: {}'.format(part1_answer)
    print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
