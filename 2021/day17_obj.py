from dataclasses import dataclass, field

import numpy as np
from rich import print


@dataclass
class Range:
    x1: int
    x2: int
    y1: int
    y2: int


@dataclass
class Probe:
    velocity: np.ndarray            # Actual object speed
    target: Range                   # Target Area
    position: np.ndarray = None     # Current position
    acceleration: np.ndarray = None # Total of all forces acting on velocity
    gravity: np.ndarray = None
    max_y: int = -float('inf')
    hit: bool = False

    def __post_init__(self):
        self.position = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.gravity = np.array([0, -1])

    def run(self):
        while self.position[0] < self.target.x2 and self.position[1] > self.target.y1:
            self.position += self.velocity

            if self.position[1] > self.max_y:
                self.max_y = self.position[1]

            if self.target.x1 <= self.position[
                0] <= self.target.x2 and self.target.y1 <= self.position[
                    1] <= self.target.y2:
                self.hit = True
                break

            self.apply_forces()

    def apply_forces(self):
        self.apply_drag()
        self.apply_gravity()
        self.velocity += self.acceleration
        self.acceleration *= 0

    def apply_gravity(self):
        self.acceleration += self.gravity

    def apply_drag(self):
        if self.velocity[0] > 0:
            self.acceleration += np.array([-1, 0])
        elif self.velocity[0] < 0:
            self.acceleration += np.array([1, 0])


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [[int(i.strip(','))
                 for i in y.split('=')[1].split('..')]
                for x in f.readlines()
                for y in x.split()[-2:]]


def main():
    data = get_data('day17.txt')
    t_range = Range(data[0][0], data[0][1], data[1][0], data[1][1])

    max_y = -float('inf')
    velocities = set()
    for y in range(-100, 100):
        for x in range(t_range.x1 * 100):
            probe = Probe(np.array([x, y]), t_range)
            probe.run()
            if probe.hit:
                velocities.add((x, y))
                if probe.max_y > max_y:
                    max_y = probe.max_y

    print(f'PART 1: {max_y}')
    print(f'PART 2: {len(velocities)}')


if __name__ == "__main__":
    main()
