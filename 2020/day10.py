from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sorted(map(int, f.read().splitlines()))


def part1(data):
    one = three = 0
    for idx in range(1, len(data)):
        if data[idx] - data[idx - 1] == 1:
            one += 1
        if data[idx] - data[idx - 1] == 3:
            three += 1
    return (one * three)


def part2(data):
    # find largest gap
    left, right = 0, 1
    count = 0
    while right < len(data):
        if data[right] - data[left] > 3:
            print(data[left])
            count += right - 2 - left
            left = right - 1
            continue
        right += 1
        if right > len(data):
            # left = data[-1]
            break
    while left < len(data):
        print(data[left])
        left += 1
    print(2**count)


def main():
    data = get_data('day10.txt')
    data = [0, *data, data[-1] + 3]
    print(f'PART 1: {part1(data)}')
    part2(data)


if __name__ == "__main__":
    main()
