
import hashlib


def generate_password(door_id, password_length):

    index = 0
    password = ''
    while len(password) < password_length:
        md5 = hashlib.md5(door_id + str(index)).hexdigest()
        if md5.startswith('00000'):
            password += md5[5]
        index += 1
    return password


def generate_password2(door_id, password_length):

    index = 0
    password = ''.join('_' for _ in range(0, password_length))
    while '_' in password:
        md5 = hashlib.md5(door_id + str(index)).hexdigest()
        if md5.startswith('00000'):
            try:
                position = int(md5[5])
                character = md5[6]
                if password[position] == '_':
                    password = password[:position] + character + password[position + 1:]
            except (IndexError, ValueError):
                pass  # ignore invalid positions
        index += 1
    return password


def solve():
    door_id = 'uqwqemis'
    part1_answer = generate_password(door_id, 8)
    part2_answer = generate_password2(door_id, 8)
    print 'Part One Answer: {}'.format(part1_answer)
    print 'Part Two Answer: {}'.format(part2_answer)


if __name__ == '__main__':
    solve()
