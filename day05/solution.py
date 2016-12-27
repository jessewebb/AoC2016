
import hashlib
import time


def generate_password(door_id, password_length):

    def _gen_password_chars():
        i = 0
        num_chars_generated = 0
        while num_chars_generated < password_length:
            md5 = hashlib.md5(door_id + str(i)).hexdigest()
            i += 1
            if md5.startswith('00000'):
                num_chars_generated += 1
                yield md5[5]

    return ''.join(_gen_password_chars())


def generate_password2(door_id, password_length):

    index = 0
    password = ''
    while len(password) < password_length:
        md5 = hashlib.md5(door_id + str(index)).hexdigest()
        if md5.startswith('00000'):
            password += md5[5]
        index += 1
    return password


def solve():
    door_id = 'uqwqemis'
    a1_t0 = time.time()
    part1_answer1 = generate_password(door_id, 8)
    a1_t1 = time.time()
    a2_t0 = time.time()
    part1_answer2 = generate_password2(door_id, 8)
    a2_t1 = time.time()
    # part2_answer = foo(puzzle_input)
    print 'Part One Answer1: {} ({})'.format(part1_answer1, str(a1_t1-a1_t0))
    print 'Part One Answer2: {} ({})'.format(part1_answer2, str(a2_t1-a2_t0))
    # print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
