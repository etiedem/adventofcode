import pathlib

import pytest

import day11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.Map.from_str(aoc.get_data(puzzle_input))


def test_parse_example(example):
    assert example.galaxy_distance == 374


def test_answer_example(example):
    example.find_dist_to_neighbours(100)
    answer = example.galaxy_distance
    assert answer == 8410
