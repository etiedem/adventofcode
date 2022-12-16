from copy import deepcopy
from dataclasses import dataclass, field

from rich import print


@dataclass
class Enhance:
    algo: list = field(default_factory=list)
    image: list = field(default_factory=list)

    def get_area(self, x, y, image):
        lookup = ((-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1),
                  (1, 1))

        result = ''
        for dx, dy in lookup:
            try:
                item = image[y + dy][x + dx]
            except IndexError:
                item = '.'
            result += item
        return result

    def get_pixel(self, x, y, image):
        idx = int(self.get_area(x, y, image).replace('#', '1').replace('.', '0'), 2)
        return self.algo[idx]

    def expand(self, image):
        new_image = deepcopy(image)
        ADD = 1
        # Add 4 empty to the left and right
        for y in range(len(new_image)):
            for _ in range(ADD):
                new_image[y].insert(0, '.')
                new_image[y].insert(len(new_image[y]), '.')
        for _ in range(ADD):
            new_image.append(['.'] * len(new_image[0]))
            new_image = [deepcopy(new_image[-1]), *new_image]

        return new_image

    def collapse(self, image):
        new_image = [row for row in image if '#' in row]

        min_x = len(image[0])
        max_x = 0

        for row in new_image:
            for x, item in enumerate(row):
                if item == '#':
                    min_x = min(x, min_x)
                    max_x = max(x, max_x)

        for y, row in enumerate(new_image):
            new_image[y] = new_image[y][min_x:max_x + 1]

        return new_image

    def enhance(self):
        test_image = self.expand(deepcopy(self.image))
        new_image = deepcopy(test_image)
        for y in range(len(test_image)):
            for x in range(len(test_image[0])):
                new_image[y][x] = self.get_pixel(x, y, test_image)

        self.image = self.collapse(new_image)

    @property
    def lit(self):
        return sum(row.count('#') for row in self.image)

    def show(self, image=None):
        image = image or self.image
        for row in image:
            for item in row:
                print(item, end='')
            print()


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        algo, image = f.read().split('\n\n')

        algo = list(algo)
        image = [list(line) for line in image.split()]

        return algo, image


def main():
    data = get_data('day20.txt')
    enhance = Enhance(data[0], data[1])
    enhance.enhance()
    enhance.enhance()
    enhance.show()
    print(enhance.lit)


if __name__ == "__main__":
    main()
