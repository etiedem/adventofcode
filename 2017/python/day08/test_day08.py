import pathlib

import day08 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def instr(example):
    return [aoc.Instr.from_str(x) for x in example.splitlines()]


def test_parse_example(instr):
    answer = [
        aoc.Instr("b", "inc", 5, ["a", ">", "1"]),
        aoc.Instr("a", "inc", 1, ["b", "<", "5"]),
        aoc.Instr("c", "dec", -10, ["a", ">=", "1"]),
        aoc.Instr("c", "inc", -20, ["c", "==", "10"]),
    ]
    assert instr == answer


def test_answer_example(instr):
    answer1, answer2 = aoc.solve(instr)
    assert answer1 == 1
    assert answer2 == 10
