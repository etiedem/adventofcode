from copy import deepcopy

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [x.split() for x in f.read().splitlines()]


def part_1(data):
    count = 0
    seen = set()
    pos = 0
    end = len(data)
    while pos not in seen and pos < end:
        current = data[pos]
        seen.add(pos)
        if current[0] == 'nop':
            pos += 1
        elif current[0] == 'acc':
            pos += 1
            count += int(current[1])
        elif current[0] == 'jmp':
            if current[1][0] == '+':
                pos += int(current[1][1:])
            else:
                pos -= int(current[1][1:])
    return count, pos >= end


def part_2(data):
    for idx in range(len(data)):
        if data[idx][0] not in ('nop', 'jmp'):
            continue

        current = deepcopy(data)
        if data[idx][0] == 'nop':
            current[idx][0] = 'jmp'
        elif data[idx][0] == 'jmp':
            current[idx][0] = 'nop'

        test, fin = part_1(current)
        if fin:
            return test


def main():
    data = get_data('day8.txt')
    print(f'PART 1: {part_1(data)[0]}')
    print(f'PART 2: {part_2(data)}')


if __name__ == "__main__":
    main()
