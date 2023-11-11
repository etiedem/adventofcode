import pathlib

import day09 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "input, expected",
    [
        ("{}", 1),
        ("{{{}}}", 6),
        ("{{},{}}", 5),
        ("{{{},{},{{}}}}", 16),
        ("{<a>,<a>,<a>,<a>}", 1),
        ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ],
)
def test_get_score(input, expected):
    answer = aoc.Tree.from_str(input).get_score()
    assert answer == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("{<>}", 0),
        ("{<random characters>}", 17),
        ("{<<<<>}", 3),
        ("{<{!>}>}", 2),
        ("{<!!>}", 0),
        ("{<!!!>>}", 0),
        ('{<{o"i!a,<{i<a>}', 10),
    ],
)
def test_count_garbage(input, expected):
    answer = aoc.Tree.from_str(input).count_garbage()
    assert answer == expected
