from collections import Counter, defaultdict

from rich import print


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(y) for x in f.readlines() for y in x.split(',')]


def take_turn(bucket):
    new_bucket = defaultdict(int)
    for k, v in bucket.items():
        if k == 0:
            new_bucket[6] += v
            new_bucket[8] += v
        else:
            new_bucket[k - 1] += v
    return new_bucket


def main():
    data = get_data('day6.txt')
    bucket = Counter(data)
    for _ in range(256):
        bucket = take_turn(bucket)
    print(sum(bucket.values()))


if __name__ == "__main__":
    main()
