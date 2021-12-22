from collections import defaultdict
from dataclasses import dataclass, field

from rich import print


@dataclass(slots=True)
class Polymer:
    base: str
    rules: dict
    counter: dict = field(default_factory=dict)

    def __post_init__(self):
        self.counter = {rule: 0 for rule in self.rules}

    def _step(self):
        new_counter = defaultdict(int)

        for rule in self.rules.items():

            if (x := rule[0][0] + rule[1]) in self.rules:
                new_counter[x] += self.counter[rule[0]]
            if (y := rule[1] + rule[0][1]) in self.rules:
                new_counter[y] += self.counter[rule[0]]
        self.counter = new_counter

    def steps(self, num):
        for x in range(len(self.base) - 1):
            if self.rules.get(self.base[x:x + 2]):
                self.counter[self.base[x:x + 2]] += 1

        for _ in range(num):
            self._step()

    def answer(self):
        answer_dict = defaultdict(int)
        for k, v in self.counter.items():
            answer_dict[k[0]] += v
            answer_dict[k[1]] += v

        answer_dict[self.base[0]] += 1
        answer_dict[self.base[-1]] += 1

        for k, v in answer_dict.items():
            answer_dict[k] = v // 2

        return max(answer_dict.values()) - min(answer_dict.values())


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        start, rules = f.read().split('\n\n')
        return start, dict([rule.split(' -> ') for rule in rules.splitlines()])


def main():
    start, rules = get_data('day14.txt')
    p = Polymer(start, rules)
    p.steps(40)
    print(p.answer())


if __name__ == "__main__":
    main()
