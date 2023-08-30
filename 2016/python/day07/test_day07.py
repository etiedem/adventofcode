import pathlib

import day07 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = PUZZLE_DIR / "example.txt"
    return aoc.get_data(puzzle_input)


@pytest.fixture
def ips(example):
    return [aoc.IP.from_str(x) for x in example.splitlines()]


def test_parse_example(example):
    ips = [aoc.IP.from_str(x) for x in example.splitlines()]
    assert ips == [
        aoc.IP(["abba", "qrst"], ["mnop"]),
        aoc.IP(["abcd", "xyyx"], ["bddb"]),
        aoc.IP(["aaaa", "tyui"], ["qwer"]),
        aoc.IP(["ioxxoj", "zxcvbn"], ["asdfgh"]),
    ]


def test_tls(ips):
    answer = [x.tls for x in ips]
    assert answer == [True, False, False, True]


@pytest.mark.parametrize(
    "input, expected",
    [("aba[bab]xyz", True), ("xyx[xyx]xyx", False), ("aaa[kek]eke", True), ("zazbz[bzb]cdb", True)],
)
def test_ssl(input, expected):
    answer = aoc.IP.from_str(input).ssl
    assert answer == expected
