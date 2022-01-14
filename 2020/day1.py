from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(map(int, f.read().split()))


def main():
    TARGET = 2020

    data = get_data('day1.txt')
    for x in range(len(data) - 2):
        for y in range(1, len(data) - 1):
            for z in range(2, len(data)):
                if data[x] + data[y] + data[z] == TARGET:
                    print(data[x] * data[y] * data[z])
                    return


if __name__ == "__main__":
    main()
