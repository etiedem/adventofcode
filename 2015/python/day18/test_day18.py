import pathlib

import day18 as aoc
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def grid(example):
    return aoc.Grid.from_str(example)


def test_parse_example(grid):
    assert np.array_equal(
        grid.grid,
        aoc.Grid(
            [
                [0, 1, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 1, 1, 1, 0, 0],
            ]
        ).grid,
    )


@pytest.mark.parametrize("x, y, expected", [(3, 1, 2), (2, 5, 3), (0, 2, 0), (5, 2, 1)])
def test_answer_example(x, y, expected, grid):
    assert grid._check_nei(x, y) == expected


def test_answer_step_1(grid):
    assert np.array_equal(
        grid.step(1).grid,
        aoc.Grid(
            [
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 0],
            ]
        ).grid,
    )


def test_answer_step_4(grid):
    assert np.array_equal(
        grid.step(4).grid,
        aoc.Grid(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        ).grid,
    )


def test_answer_lights_step_4(grid):
    assert grid.step(4).lights == 4


def test_answer_step_1_p2(grid):
    assert np.array_equal(
        grid.turn_on_corners().step(1, 2).grid,
        aoc.Grid(
            [
                [1, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0],
                [1, 0, 1, 1, 1, 1],
            ]
        ).grid,
    )
