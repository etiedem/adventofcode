from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(map(int, f.read().splitlines()))


def is_sum(data, target):
    for num in data:
        if target - num in data:
            return True
    # for left in range(len(data) - 1):
    #     for right in range(left + 1, len(data)):
    #         if data[left] + data[right] == target:
    #             return True


def find_error(data, size):
    for x in range(len(data) - size - 1):
        if not is_sum(data[x:x + size], data[x + size]):
            return data[x + size]


def main():
    data = get_data('day9.txt')
    print(find_error(data, 25))


if __name__ == "__main__":
    main()
