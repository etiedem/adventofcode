from copy import copy
from dataclasses import dataclass, field

from rich import print


@dataclass(slots=True)
class Parser:
    _raw: str
    base: str = ''
    packets: list = field(default_factory=list)
    version_sum: int = 0

    def __post_init__(self):
        self.base = self._raw
        self.run()

    def get_header(self):
        version = int(self.base[:3], 2)
        self.version_sum += version
        t_id = self.base[3:6]
        self.base = self.base[6:]
        return Header(version, int(t_id, 2))

    def parse_literal(self):
        result = ''
        while True:
            term, d = self.base[0], self.base[1:5]
            result += d
            self.base = self.base[5:]
            if term == '0':
                break
        return int(result, 2)

    def parse_type_0(self):
        # Next 15 bits are sub-packets
        length = int(self.base[:15], 2)
        tmp = self.base[15:length + 15]
        self.base = self.base[length + 15:]
        parser = Parser(tmp)
        self.version_sum += parser.version_sum
        return parser.packets

    def parse_type_1(self):
        # Next number of 11 bits are sub-packets
        length = int(self.base[:11], 2)
        self.base = self.base[11:]
        return [self.parse_packets() for _ in range(length)]

    def parse_operator(self):
        l_id = self.base[0]
        self.base = self.base[1:]
        if l_id == '0':
            packets = self.parse_type_0()
        elif l_id == '1':
            packets = self.parse_type_1()
        else:
            raise ValueError
        return packets

    def parse_packets(self):
        header = self.get_header()
        if header.t_id == 4:
            return Packet(header, self.parse_literal())
        return Packet(header, None, self.parse_operator())

    def run(self):
        while self.base:
            if len(self.base) < 8:
                break
            self.packets.append(self.parse_packets())


@dataclass(slots=True)
class Header:
    version: int
    t_id: int


@dataclass(slots=True)
class Packet:
    header: Header
    data: int
    subpackets: list = field(default_factory=list)


def flatten(container):
    for i in container:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        digit = f.read().strip()
        size = len(digit) * 4
        return (bin(int(digit, 16))[2:]).zfill(size)


def main():
    data = get_data('day16.txt')
    parser = Parser(data)
    print(parser.packets)
    print(parser.version_sum)


if __name__ == "__main__":
    main()
