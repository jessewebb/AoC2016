
from itertools import permutations


def count_possible_triangles(triangles_input):
    count = 0
    for triangle_input in triangles_input.splitlines():
        triangle_sides = [int(side) for side in triangle_input.split()]
        assert len(triangle_sides) == 3, "invalid input: {}".format(triangle_input)
        if _is_possible_triangle(triangle_sides):
            count += 1
    return count


def _is_possible_triangle(triangle_sides):
    return all([p[0] + p[1] > p[2] for p in permutations(triangle_sides)])


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = count_possible_triangles(puzzle_input)
    print 'Part One Answer: {}'.format(part1_answer)


if __name__ == '__main__':
    solve()
