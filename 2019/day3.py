from pyparsing import Char, Group, LineEnd, OneOrMore, Suppress, common
from rich import print


def get_data(filename):
    # R75,D30,R83,U83,L12,D49,R71,U7,L72
    direction = Group(Char('LRUD') + common.integer)
    parser = OneOrMore(
        Group(
            OneOrMore(direction + Suppress(',')) + direction +
            LineEnd().suppress()))
    return parser.parse_file(filename)


def create_paths(data):
    paths = []
    for line in data:
        x = y = 0
        path = set()
        for item in line:
            match item:
                case ['R', step]:
                    for _ in range(step):
                        x += 1
                        path.add((x, y))
                case ['L', step]:
                    for _ in range(step):
                        x -= 1
                        path.add((x, y))
                case ['U', step]:
                    for _ in range(step):
                        y += 1
                        path.add((x, y))
                case ['D', step]:
                    for _ in range(step):
                        y -= 1
                        path.add((x, y))
        paths.append(path)
    return paths


def main():
    data = get_data('day3.txt')
    paths = create_paths(data)
    inter = set.intersection(*paths)
    print(min(abs(x)+abs(y) for x, y in inter))


if __name__ == "__main__":
    main()
