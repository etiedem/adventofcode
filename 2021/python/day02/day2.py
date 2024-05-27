from rich import print


def get_position(data):
    depth, forward, aim = 0, 0, 0
    for pos in data:
        match pos.split():
            case ['forward', step]:
                forward += int(step)
                depth += aim * int(step)
            case ['up', step]:
                aim -= int(step)
            case ['down', step]:
                aim += int(step)
            case _:
                raise ValueError
    return depth * forward


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [x.strip() for x in f.readlines()]


def main():
    data = get_data(r'day2.txt')
    print(get_position(data))


if __name__ == "__main__":
    main()
