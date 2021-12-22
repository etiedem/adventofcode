from collections import Counter, defaultdict
from dataclasses import dataclass

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(y) for x in f.readlines() for y in x.split(',')]


@dataclass
class Bucket:
    bucket: dict

    def take_turn(self):
        new_bucket = defaultdict(int)
        for k, v in self.bucket.items():
            if k == 0:
                new_bucket[6] += v
                new_bucket[8] += v
            else:
                new_bucket[k - 1] += v
        self.bucket = new_bucket

    def turns(self, turns):
        for _ in range(turns):
            self.take_turn()

    @property
    def crabs(self):
        return sum(self.bucket.values())


def main():
    data = get_data('day6.txt')
    bucket = Bucket(Counter(data))
    bucket.turns(256)
    print(bucket.crabs)


if __name__ == "__main__":
    main()
