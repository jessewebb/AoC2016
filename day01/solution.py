
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


def calculate_shortest_grid_distance(instructions, stop_at_first_location_visited_twice=False):
    direction = Direction.North
    current_position = (0, 0)
    visited_positions = [current_position]
    steps = instructions.split(', ')
    for step in steps:
        turn = step[0]
        blocks = int(step[1:])
        direction = _determine_new_direction(direction, turn)
        for _ in range(0, blocks):
            current_position = tuple(pos + change for pos, change in zip(current_position, BEARINGS[direction]))
            if stop_at_first_location_visited_twice and current_position in visited_positions:
                break
            visited_positions.append(current_position)

    (x, y) = current_position
    shortest_grid_distance = abs(x) + abs(y)
    return shortest_grid_distance


def _determine_new_direction(current_direction, turn):
    value_change = 1 if turn == 'R' else -1
    new_direction_value = current_direction.value + value_change
    return Direction(abs(new_direction_value % 4))


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = calculate_shortest_grid_distance(puzzle_input)
    part2_answer = calculate_shortest_grid_distance(puzzle_input, stop_at_first_location_visited_twice=True)
    print 'Part One Answer: {}'.format(part1_answer)
    print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
