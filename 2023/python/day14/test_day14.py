import pathlib

import pytest

import day14 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.parse(aoc.get_data(puzzle_input))


def test_answer_example(example):
    answer = aoc.calc_load(aoc.part1(example))
    assert answer == 136


def test_answer_example1(example):
    grid, start, cycle_length = aoc.find_repeating(example)
    remaining = (1_000_000_000 - start) % cycle_length
    answer = aoc.calc_load(aoc.part2(grid, remaining))
    assert answer == 64

