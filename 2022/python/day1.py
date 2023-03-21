from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for x in f:
            yield x.strip()


def largest(data, num):
    return sum(sum(x) for x in sorted(data, key=sum, reverse=True)[:num])


def main():
    elf = []
    tmp = []
    for calorie in get_data(r"day1.txt"):
        if calorie:
            tmp.append(int(calorie))
        else:
            elf.append(tmp)
            tmp = []

    print(f"PART1: {largest(elf, 1)}")
    print(f"PART2: {largest(elf, 3)}")


if __name__ == "__main__":
    main()
