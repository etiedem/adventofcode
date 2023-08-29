import pathlib

import day04 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def rooms(example):
    return [aoc.Room.from_str(x) for x in example.splitlines()]


def test_parse_example(example):
    rooms = [aoc.Room.from_str(x) for x in example.splitlines()]
    assert rooms == [
        aoc.Room("abxyz", 123, "aaaaa-bbb-z-y-x"),
        aoc.Room("abcde", 987, "a-b-c-d-e-f-g-h"),
        aoc.Room("oarel", 404, "not-a-real-room"),
        aoc.Room("decoy", 200, "totally-real-room"),
    ]


def test_answer_example(rooms):
    assert [r.is_real() for r in rooms] == [True, True, True, False]
