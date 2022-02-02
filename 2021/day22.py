from re import split

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [split(r'[ ,=]', line)[::2] for line in f.read().splitlines()]


def expand(_x, _y, _z):
    xmin, xmax = map(int, _x.split('..'))
    ymin, ymax = map(int, _y.split('..'))
    zmin, zmax = map(int, _z.split('..'))

    if any(check < -50 for check in [xmin, ymin, zmin]):
        return set()

    if any(check > 50 for check in [xmax, ymax, zmax]):
        return set()

    result = set()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                result.add((x, y, z))

    return result


def part1(data):
    result = set()
    for action, x, y, z in data:
        _range = expand(x, y, z)
        if action == 'on':
            result = result.union(_range)
        elif action == 'off':
            result = result - _range
    return len(result)


def main():
    data = get_data('day22.txt')
    print(part1(data))


if __name__ == "__main__":
    main()
