import pathlib

import day11 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "input, expected",
    [("ne,ne,ne", (3, 3)), ("ne,ne,sw,sw", (0, 2)), ("ne,ne,s,s", (2, 2))],
)
def test_answer_example(input, expected):
    answer1, answer2 = aoc.solve(input)
    assert answer1 == expected[0]
    assert answer2 == expected[1]
