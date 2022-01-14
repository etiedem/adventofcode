from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [
            set(y
                for x in group.split()
                for y in x)
            for group in f.read().split('\n\n')
        ]


def main():
    data = get_data('day6.txt')
    print(sum(len(x) for x in data))


if __name__ == "__main__":
    main()
