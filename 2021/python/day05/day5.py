from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[list(map(int, y.split(',')))
                 for y in x.strip().split('->')]
                for x in f.readlines()]


def get_largest(data):
    x, y = 0, 0
    for line in data:
        for point in line:
            if point[0] > x:
                x = point[0]
            if point[1] > y:
                y = point[1]
    return x + 10, y + 10


def create_matrix(x, y):
    return [[0] * x for _ in range(y)]


def get_moves(point1, point2):
    result = [point1]
    x1, y1 = point1
    x2, y2 = point2

    while x1 != x2 or y1 != y2:
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1

        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        result.append([x1, y1])
    return result


def make_moves(moves, matrix):
    for x, y in moves:
        try:
            matrix[x][y] += 1
        except IndexError:
            print(moves)


def update_matrix(data, matrix):
    for point1, point2 in data:
        moves = get_moves(point1, point2)
        make_moves(moves, matrix)


def find_danger(matrix):
    count = 0
    for line in matrix:
        for num in line:
            if num > 1:
                count += 1
    return count


def main():
    vents = get_data('day5.txt')
    matrix = create_matrix(*get_largest(vents))
    update_matrix(vents, matrix)
    print(find_danger(matrix))


if __name__ == "__main__":
    main()
