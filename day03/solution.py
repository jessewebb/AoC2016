
from itertools import permutations


def count_possible_triangles(triangles_input, vertically=False):
    count = 0
    triangles = _split_triangles(triangles_input, vertically)
    for triangle in triangles:
        if _is_valid_triangle(triangle):
            count += 1
    return count


def _split_triangles(triangles_input, vertically):
    matrix = [tuple(int(side) for side in line_of_input.split()) for line_of_input in triangles_input.splitlines()]
    if vertically:
        return [tuple(matrix[y+s][x] for s in range(0, 3))
                for y in range(0, len(matrix), 3)
                for x in range(0, len(matrix[0]))]
    else:
        return matrix


def _is_valid_triangle(triangle):
    return all([p[0] + p[1] > p[2] for p in permutations(triangle)])


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = count_possible_triangles(puzzle_input)
    part2_answer = count_possible_triangles(puzzle_input, vertically=True)
    print 'Part One Answer: {}'.format(part1_answer)
    print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
