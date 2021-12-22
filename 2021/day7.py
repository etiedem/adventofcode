import math
import statistics

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(y) for x in f.readlines() for y in x.split(',')]


def partial_sum(num):
    return sum(range(num + 1))


def get_cost(data, pos):
    return sum(partial_sum(abs(crab - pos)) for crab in data)


def main():
    data = get_data('day7.txt')
    mean = math.ceil(statistics.mean(data))
    print(min(get_cost(data, pos) for pos in range(mean - 10, mean + 10)))


if __name__ == "__main__":
    main()
