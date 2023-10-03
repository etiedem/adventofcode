import pathlib

import day17 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def maze():
    puzzle_input = aoc.get_data(PUZZLE_DIR / "maze.txt")
    return aoc.Maze(puzzle_input, "hijkl")


@pytest.fixture
def maze_raw():
    puzzle_input = aoc.get_data(PUZZLE_DIR / "maze.txt")
    return puzzle_input


@pytest.mark.parametrize(
    "input, expected",
    [
        ([(1, 1), ""], [("D", (3, 1))]),
        ([(3, 1), "D"], [("R", (3, 3)), ("U", (1, 1))]),
        ([(3, 3), "DR"], []),
        ([(1, 1), "DU"], [("R", (1, 3))]),
    ],
)
def test_maze_neighbors(maze, input, expected):
    answer = list(maze.get_neigh(*input))
    assert answer == expected


@pytest.mark.parametrize(
    "passcode, expected",
    [
        ("ihgpwlah", "DDRRRD"),
        ("kglvqrro", "DDUDRLRRUDRD"),
        ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
    ],
)
def test_maze_solve_shortest(maze_raw, passcode, expected):
    answer = aoc.solve_shortest(maze_raw, passcode).path
    assert answer == expected


@pytest.mark.parametrize(
    "passcode, expected",
    [
        ("ihgpwlah", 370),
        ("kglvqrro", 492),
        ("ulqzkmiv", 830),
    ],
)
def test_maze_solve_longest(maze_raw, passcode, expected):
    answer = aoc.solve_longest(maze_raw, passcode)
    assert answer == expected
