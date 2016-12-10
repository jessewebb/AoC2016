
PART_ONE_KEYPAD = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

PART_TWO_KEYPAD = [
    [None, None, '1', None, None],
    [None, '2',  '3', '4',  None],
    ['5',  '6',  '7', '8',  '9'],
    [None, 'A',  'B', 'C',  None],
    [None, None, 'D', None, None],
]

_STARTING_KEY = '5'


_MOVEMENTS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}


def calculate_keypad_code(instructions, keypad):
    current_keypad_position = find_position_of_key(keypad, _STARTING_KEY)
    result = ''
    for instruction_line in instructions.splitlines():
        for movement in instruction_line:
            current_keypad_position = _determine_new_keypad_position(keypad, current_keypad_position, movement)
        result += _get_key_at_position(keypad, current_keypad_position)
    return result


def find_position_of_key(keypad, key):
    return next((i, row.index(key)) for i, row in enumerate(keypad) if key in row)


def _determine_new_keypad_position(keypad, current_position, movement):

    def _adjust_position_index(index, change):
        new_index = index + change
        if new_index < 0 or new_index >= len(keypad):  # assumes the keypad is square
            return index
        return new_index

    new_position = tuple(_adjust_position_index(pos, change)
                         for pos, change in zip(current_position, _MOVEMENTS[movement]))
    return new_position if _get_key_at_position(keypad, new_position) else current_position


def _get_key_at_position(keypad, position):
    return keypad[position[0]][position[1]]


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = calculate_keypad_code(puzzle_input, PART_ONE_KEYPAD)
    part2_answer = calculate_keypad_code(puzzle_input, PART_TWO_KEYPAD)
    print 'Part One Answer: {}'.format(part1_answer)
    print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
