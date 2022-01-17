from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(map(int, f.read().splitlines()))


def is_sum(data, target):
    for num in data:
        if target - num in data:
            return True


def find_sum(data, target):
    for left in range(len(data) - 1):
        sum = data[left]
        mn = mx = data[left]
        for right in range(left + 1, len(data)):
            sum += data[right]
            if sum > target:
                break
            mn = min(mn, data[right])
            mx = max(mx, data[right])
            if sum == target:
                return mn + mx


def find_error(data, size):
    for x in range(len(data) - size - 1):
        if not is_sum(data[x:x + size], data[x + size]):
            return data[x + size]


def main():
    data = get_data('day9.txt')
    part1 = find_error(data, 25)
    print(f'PART 1: {part1}')
    print(f'PART 2: {find_sum(data, part1)}')


if __name__ == "__main__":
    main()
