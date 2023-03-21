from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def tree_map(data):
    result = set()
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "#":
                result.add((x, y))
    return result, x


def extend_map(trees, base, max_x):
    result = {(x + base + 1, y) for x, y in trees if max_x - base <= x <= max_x}
    return trees.union(result)


def get_slope(trees, my, base, slope):
    max_x = base
    x = y = count = 0
    dx, dy = slope
    while y < my:
        y += dy
        x += dx
        if x > max_x:
            trees = extend_map(trees, base, max_x)
            max_x += base
        if (x, y) in trees:
            count += 1
    return count


def main():
    data = get_data("day3.txt")
    trees, base = tree_map(data)

    print(f"PART 1: {get_slope(trees, len(data), base, (3,1))}")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for slope in slopes:
        result *= get_slope(trees, len(data), base, slope)
    print(f"PART 2: {result}")


if __name__ == "__main__":
    main()
