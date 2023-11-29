import pathlib

import day17 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return "3"


def test_answer_example(example):
    answer = aoc.part1(int(example))
    assert answer == 638
