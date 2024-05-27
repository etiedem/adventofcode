from dataclasses import dataclass

# from rich import print


@dataclass
class Pos:
    x: int = 0
    y: int = 0


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(i.strip(','))
                 for i in y.split('=')[1].split('..')]
                for x in f.readlines()
                for y in x.split()[-2:]]


def step(x_v, y_v, target_x, target_y):
    pos = Pos()
    tx_v = x_v # X velocity
    ty_v = y_v # Y velocity

    max_y = -float('inf')

    while pos.x < target_x[1] and pos.y > target_y[0]:
        pos.x += tx_v
        pos.y += ty_v

        if pos.y > max_y:
            max_y = pos.y

        if target_x[0] <= pos.x <= target_x[1] and target_y[0] <= pos.y <= target_y[1]:
            return max_y

        # Drag
        if tx_v > 0:
            tx_v -= 1
        elif tx_v < 0:
            tx_v += 1

        ty_v -= 1 # Gravity


def main():
    data = get_data('day17.txt')
    target_x, target_y = data

    max_y = -float('inf')
    velocities = set()
    for y in range(-100, 100):
        for x in range(target_x[1] * 100):
            tmp = step(x, y, target_x, target_y)
            if tmp is not None:
                velocities.add((x, y))
                if tmp > max_y:
                    max_y = tmp
    print(max_y)
    print(len(velocities))


if __name__ == "__main__":
    main()
