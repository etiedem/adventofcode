from copy import copy
from dataclasses import dataclass, field

from rich import print


@dataclass(slots=True)
class Parser:
    _raw: str
    base: str = ''
    packets: list = field(default_factory=list)

    def __post_init__(self):
        self.base = self._raw
        self.parse_packets()

    def get_header(self):
        version = self.base[:3]
        t_id = self.base[3:6]
        self.base = self.base[6:]
        return Header(int(version, 2), int(t_id, 2))

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
        return Parser(tmp).packets

    def parse_type_1(self):
        # Next number of 11 bits are sub-packets
        length = int(self.base[:11], 2)
        tmp = self.base[11:(11*length) + 11]
        self.base = self.base[(11*length) + 11:]
        return Parser(tmp).packets

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
        while self.base:
            if len(self.base) < 8:
                break
            header = self.get_header()
            if header.t_id == 4:
                d = self.parse_literal()
                self.packets.append(Packet(header, d))
            else:
                packets = self.parse_operator()
                self.packets.append(Packet(header, None, packets))


@dataclass(slots=True)
class Header:
    version: int
    t_id: int


@dataclass(slots=True)
class Packet:
    header: Header
    data: int
    subpackets: list = field(default_factory=list)


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        digit = f.read().strip()
        size = len(digit) * 4
        return (bin(int(digit, 16))[2:]).zfill(size)


def main():
    data = get_data('day16.txt')
    parser = Parser(data)
    # packets = parse_packets(data)
    # print(parser._raw)
    print(parser.packets)


if __name__ == "__main__":
    main()
