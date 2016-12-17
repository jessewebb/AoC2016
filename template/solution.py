
def foo(arg):
    raise NotImplementedError


def solve():
    with open('puzzle_input.txt') as puzzle_input_file:
        puzzle_input = puzzle_input_file.read()
    part1_answer = foo(puzzle_input)
    # part2_answer = foo(puzzle_input)
    print 'Part One Answer: {}'.format(part1_answer)
    # print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
