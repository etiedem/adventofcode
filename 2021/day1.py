from rich import print


def get_increase(data):
    for x in range(len(data) - 3):
        a_win, b_win = data[x:x + 3], data[x + 1:x + 4]
        if sum(b_win) > sum(a_win):
            yield b_win


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(x.strip()) for x in f.readlines()]


def main():
    data = get_data(r'day1.txt')
    print(len(list(get_increase(data))))


if __name__ == "__main__":
    main()
