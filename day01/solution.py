
from enum import Enum


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


BEARINGS = {
    Direction.North: (0, 1),
    Direction.East: (1, 0),
    Direction.South: (0, -1),
    Direction.West: (-1, 0),
}


def calculate_shortest_grid_distance(instructions):
    direction = Direction.North
    current_position = (0, 0)
    steps = instructions.split(', ')
    for step in steps:
        turn = step[0]
        blocks = int(step[1:])
        direction = _determine_new_direction(direction, turn)
        current_position = _determine_new_position(current_position, direction, blocks)

    (x, y) = current_position
    shortest_grid_distance = abs(x) + abs(y)
    return shortest_grid_distance


def _determine_new_direction(current_direction, turn):
    value_change = 1 if turn == 'R' else -1
    new_direction_value = current_direction.value + value_change
    return Direction(abs(new_direction_value % 4))


def _determine_new_position(current_position, direction, blocks):
    change_of_position = tuple(x * int(blocks) for x in BEARINGS[direction])
    current_position = tuple(pos + change for pos, change in zip(current_position, change_of_position))
    return current_position


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    answer = calculate_shortest_grid_distance(puzzle_input)
    print answer


if __name__ == '__main__':
    solve()
