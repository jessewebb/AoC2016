
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
                if x_letter < y_letter:
                    return -1
                elif x_letter > y_letter:
                    return 1
                else:
                    return 0

        encrypted_name_letters = [char for char in self.encrypted_name if char.isalpha()]
        letter_counter = Counter(encrypted_name_letters)
        most_common_letters_and_counts = letter_counter.most_common()
        sorted_most_common_letters_and_counts = sorted(most_common_letters_and_counts, cmp=_compare_letter_counts)
        five_most_common_letters = [letter for letter, count in sorted_most_common_letters_and_counts][:5]
        checksum_letters = [letter for letter in self.checksum]
        return five_most_common_letters == checksum_letters

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


def calculate_sum_of_real_room_sector_ids(list_of_rooms_as_text):
    rooms = [Room.from_input_line(room_input_line) for room_input_line in list_of_rooms_as_text.splitlines()]
    return sum(room.sector_id for room in rooms if room.is_real)


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = calculate_sum_of_real_room_sector_ids(puzzle_input)
    # part2_answer = foo(puzzle_input)
    print 'Part One Answer: {}'.format(part1_answer)
    # print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
