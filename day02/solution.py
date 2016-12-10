
_KEYPAD_MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

_STARTING_POSITION = (1, 1)


_MOVEMENTS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}


def calculate_keypad_code(instructions):
    current_keypad_position = _STARTING_POSITION
    result = ''
    for instruction_line in instructions.splitlines():
        for movement in instruction_line:
            current_keypad_position = _determine_new_keypad_position(current_keypad_position, movement)
        result += str(_KEYPAD_MATRIX[current_keypad_position[0]][current_keypad_position[1]])
    return result


def _determine_new_keypad_position(current_position, movement):

    def _adjust_position_index(index, change):
        new_index = index + change
        if new_index < 0 or new_index > 2:
            return index
        return new_index

    return tuple(_adjust_position_index(pos, change) for pos, change in zip(current_position, _MOVEMENTS[movement]))


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = calculate_keypad_code(puzzle_input)
    print 'Part One Answer: {}'.format(part1_answer)


if __name__ == '__main__':
    solve()
