import pathlib

import day18 as aoc
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 1, 0], True),
        ([0, 1, 1], True),
        ([1, 0, 0], True),
        ([0, 0, 1], True),
        ([1, 0, 1], False),
        ([1, 1, 1], False),
    ],
)
def test_check_trap(input, expected):
    assert aoc.check_trap(*input) == expected


@pytest.mark.parametrize(
    "input, expected", [(("..^^.", 3), [[0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 0, 0, 1]])]
)
def test_make_grid(input, expected):
    answer = aoc.make_grid(*input)
    assert np.array_equal(answer, expected)


@pytest.mark.parametrize("input, expected", [(("..^^.", 3), "..^^.\n.^^^^\n^^..^")])
def test_show_grid(input, expected):
    answer = aoc.show(aoc.make_grid(*input))
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
