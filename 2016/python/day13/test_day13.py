import pathlib

import day13 as aoc
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def maze():
    return aoc.Maze(10, 10, 7)


def test_maze(maze):
    assert np.array_equal(
        maze,
        [
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        ],
    )


def test_maze_show(capsys, maze):
    maze.show()
    captured = capsys.readouterr()
    assert (
        captured.out == ".#.####.##\n"
        "..#..#...#\n"
        "#....##...\n"
        "###.#.###.\n"
        ".##..#..#.\n"
        "..##....#.\n"
        "#...##.###\n"
    )


def test_maze_solve(maze):
    path, length, _ = maze.find_sp((1, 1), (7, 4))
    assert length == 11
    assert path == [
        (1, 1),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 3),
        (4, 3),
        (4, 4),
        (5, 4),
        (5, 5),
        (5, 6),
        (4, 6),
        (4, 7),
    ]


def test_maze_dir(maze):
    assert tuple(maze.get_nei((0, 0))) == ((1, 0),)
    assert tuple(maze.get_nei((1, 1))) == ((2, 1), (1, 0))
