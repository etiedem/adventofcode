import pathlib
import pytest
import day06 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.mark.parametrize(
    "input, expected", [((7, 9), 4), ((15, 40), 8), ((30, 200), 9)]
)
def test_answer_example(input, expected):
    answer = aoc.calc_times(*input)
    assert answer == expected


def test_answer_example1(example):
    answer = aoc.solve(aoc.parse_part1(example))
    assert answer == 288


def test_answer_example2(example):
    answer = aoc.solve(aoc.parse_part2(example))
    assert answer == 71503
