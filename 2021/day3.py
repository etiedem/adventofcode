from functools import partial

from rich import print


def get_column(pos, data):
    return [d[pos] for d in data]


def get_most_least_common(data):
    one, zero = data.count('1'), data.count('0')
    if one >= zero:
        return '1', '0'
    return '0', '1'


def filter_out(data, pos, idx=0):
    if len(data) == 1:
        return ''.join(data[0])

    column = get_column(idx, data)
    most, least = get_most_least_common(column)
    result = [
        d for d, c in zip(data, column)
        if pos == 'high' and c == most or pos != 'high' and c == least
    ]
    return filter_out(result, pos, idx + 1)


def get_consumption(data):
    matrix = [list(x) for x in data]
    oxygen, co2 = map(partial(filter_out, matrix), ('high', 'low'))
    return int(oxygen, 2) * int(co2, 2)


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [x.strip() for x in f.readlines()]


def main():
    data = get_data(r'day3.txt')
    print(get_consumption(data))


if __name__ == "__main__":
    main()
