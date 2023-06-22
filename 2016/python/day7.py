#!/usr/bin/env python3.11

import re
from dataclasses import dataclass, field

from more_itertools import sliding_window
from rich import print


@dataclass
class IPv7:
    hypernets: list[str]
    net: list[str]
    tls: bool = field(init=False)
    ssl: bool = field(init=False)

    def __post_init__(self):
        self.tls = all(not self._find_abba(x) for x in self.hypernets) and any(
            self._find_abba(x) for x in self.net
        )
        self.ssl = self._check_ssl()

    def _check_ssl(self):
        if aba := self._find_aba(self.net):
            return bool(self._find_bab(self.hypernets, aba))
        return False

    def _find_abba(self, data):
        return any(x[0] == x[-1] and x[1] == x[2] and x[0] != x[1] for x in sliding_window(data, 4))

    def _find_aba(self, data):
        return [y for x in data for y in sliding_window(x, 3) if y[0] == y[-1] and y[0] != y[1]]

    def _find_bab(self, data, aba):
        return any(
            y[0] == item[1] and y[0] == y[-1] and y[1] == item[0]
            for item in aba
            for x in data
            for y in sliding_window(x, 3)
        )


def parse_address(line):
    hypernets = []
    rest = []
    token_spec = [
        ("ID", r"[a-z]+"),
        ("START", r"\["),
        ("STOP", r"\]"),
    ]
    token_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
    flag = False
    for mo in re.finditer(token_regex, line):
        kind = mo.lastgroup
        value = mo.group()

        if kind in ("START", "STOP"):
            flag = not flag
        elif kind == "ID" and flag:
            hypernets.append(value)
        elif kind == "ID":
            rest.append(value)
    return hypernets, rest


def get_data(filename):
    with open(filename, "r", encoding="utf8") as f:
        yield from f.readlines()


def main():
    data = get_data("day7.txt")
    ips = [IPv7(*parse_address(x.strip())) for x in data]

    part1 = sum(bool(ip.tls) for ip in ips)
    print(f"Part 1: {part1}")

    part2 = sum(bool(ip.ssl) for ip in ips)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
