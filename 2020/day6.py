from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [[set(x) for x in group.split()] for group in f.read().split("\n\n")]


def main():
    data = get_data("day6.txt")
    print(f"PART 1: {sum(len(set.union(*list(x))) for x in data)}")
    print(f"PART 2: {sum(len(set.intersection(*list(x))) for x in data)}")


if __name__ == "__main__":
    main()
