import pathlib
import re

import day12 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def real():
    puzzle_input = PUZZLE_DIR / "day12.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    assert aoc.parse(example) == None


def test_assumption_1(real):
    """Only strings as dictionary keys"""
    output = set()
    for i in re.finditer(r"(.):", real):
        output.add(i.group(1))
    assert output == set('"')


@pytest.mark.parametrize(
    "input, expected",
    [
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ],
)
def test_answer_part2(input, expected):
    answer = aoc.part2(input)
    assert answer == expected


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("input, expected", [("", "")])
def test_answer_example1(input, expected):
    answer = aoc.part2(input)
    assert answer == expected
