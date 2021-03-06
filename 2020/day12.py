from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[x[0], int(x[1:])] for x in f.read().splitlines()]


def part1(moves):
    facing = 180
    x = y = 0
    for move in moves:
        match move:
            case ['F', step]:
                if facing == 0:
                    x -= step
                elif facing == 180:
                    x += step
                elif facing == 90:
                    y += step
                elif facing == 270:
                    y -= step
                else:
                    raise ValueError(f'Do not understand {facing=} {move=}')
            case ['N', step]:
                y += step
            case ['S', step]:
                y -= step
            case ['E', step]:
                x += step
            case ['W', step]:
                x -= step
            case ['R', step]:
                facing += step
                facing %= 360
            case ['L', step]:
                facing -= step
                facing %= 360
    return abs(x) + abs(y)




def main():
    data = get_data('day12.txt')
    print(f'PART 1: {part1(data)}')


if __name__ == "__main__":
    main()
