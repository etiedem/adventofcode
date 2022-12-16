from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.split() for line in f.read().splitlines()]


def check_password_part1(line):
    l, r = map(int, line[0].split('-'))
    letter = line[1][0]
    password = line[2]
    count = 0
    for x in password:
        if x == letter:
            count += 1
        if count > r:
            return False
    return count >= l


def check_password_part2(line):
    l, r = map(int, line[0].split('-'))
    letter = line[1][0]
    password = line[2]
    return (password[l - 1] == letter) != (password[r - 1] == letter)


def main():
    data = get_data('day2.txt')
    p1_count = sum(1 for line in data if check_password_part1(line))
    p2_count = sum(1 for line in data if check_password_part2(line))
    print(f'PART1: {p1_count}')
    print(f'PART2: {p2_count}')


if __name__ == "__main__":
    main()
