from copy import deepcopy

from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [x.split() for x in f.read().splitlines()]


def part_1(data):
    count = pos = 0
    seen = set()

    while pos not in seen:
        if pos >= len(data):
            return count, True
        seen.add(pos)
        match data[pos][0]:
            case "nop":
                pos += 1
            case "acc":
                count += int(data[pos][1])
                pos += 1
            case "jmp":
                match data[pos][1][0]:
                    case "+":
                        pos += int(data[pos][1][1:])
                    case "-":
                        pos -= int(data[pos][1][1:])

    return count, False


def part_2(data):
    for idx in range(len(data)):
        if data[idx][0] not in ("nop", "jmp"):
            continue

        test = deepcopy(data)
        if data[idx][0] == "nop":
            test[idx][0] = "jmp"
        elif data[idx][0] == "jmp":
            test[idx][0] = "nop"

        count, fin = part_1(test)
        if fin:
            return count


def main():
    data = get_data("day8.txt")
    print(f"PART 1: {part_1(data)[0]}")
    print(f"PART 2: {part_2(data)}")


if __name__ == "__main__":
    main()
