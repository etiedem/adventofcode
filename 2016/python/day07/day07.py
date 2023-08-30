#!/usr/bin/env python3.11

import re
from dataclasses import dataclass, field

from more_itertools import sliding_window
from rich import print


@dataclass
class IP:
    nets: list[str] = field(default_factory=list)
    hypernets: list[str] = field(default_factory=list)
    tls: bool = field(init=False)
    ssl: bool = field(init=False)

    def __post_init__(self):
        self.tls = self.__abba(self.nets) and not self.__abba(self.hypernets)
        self.ssl = self.__bab()

    def __abba(self, data):
        return any(
            x[0] == x[3] and x[1] == x[2] and x[0] != x[1]
            for net in data
            for x in sliding_window(net, 4)
        )

    def __aba(self):
        for net in self.nets:
            for x in sliding_window(net, 3):
                if x[0] == x[2] and x[0] != x[1]:
                    yield x

    def __bab(self):
        for a in self.__aba():
            for net in self.hypernets:
                for x in sliding_window(net, 3):
                    if x[0] == a[1] and x[2] == a[1] and x[1] == a[0]:
                        return True
        return False

    @classmethod
    def from_str(cls, data):
        token_spec = [("HYPER", r"(?<=\[)\w+(?=\])"), ("NETS", r"\w+")]
        token_reg = "|".join("(?P<%s>%s)" % pair for pair in token_spec)
        nets = []
        hypernets = []
        for mo in re.finditer(token_reg, data):
            kind = mo.lastgroup
            value = mo.group()
            if kind == "HYPER":
                hypernets.append(value)
            elif kind == "NETS":
                nets.append(value)
        return IP(nets, hypernets)


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    data = get_data("day07.txt")
    ips = [IP.from_str(x) for x in data.splitlines()]

    p1 = sum(bool(ip.tls) for ip in ips)
    print(f"Part 1: {p1}")

    p2 = sum(bool(ip.ssl) for ip in ips)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
