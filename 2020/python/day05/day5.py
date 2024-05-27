from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        return f.read().splitlines()


def get_pos(data, mn, mx):
    for item in data[:-1]:
        if item in ("F", "L"):
            mx = (mn+mx) // 2
        else:
            mn = ((mn+mx) // 2) + 1
    return mn if data[-1] in ("F", "L") else mx


def get_seat(grid):
    for y, row in enumerate(grid):
        if "X" in row and "" in row:
            for x, item in enumerate(row):
                if item == "" and x > 0 and x < len(row) and row[x - 1] == "X" and row[
                    x + 1] == "X":
                    return y*8 + x
    return None


def main():
    data = get_data("day5.txt")
    print(
        f"PART 1: { max( get_pos(passport[:7], 0, 127) * 8 + get_pos(passport[7:], 0, 7) for passport in data )}"
    )

    grid = [[""] * 8 for row in range(128)]
    for passport in data:
        y = get_pos(passport[:7], 0, 127)
        x = get_pos(passport[7:], 0, 7)
        grid[y][x] = "X"

    print(f"PART 2: {get_seat(grid)}")


if __name__ == "__main__":
    main()
