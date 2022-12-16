import re

from rich import print

BAG_RE = re.compile(r'(\d+)\s(.*?)\sbag')


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.split('bags contain') for line in f.read().splitlines()]


def parse_bag(data):
    if data.startswith(' no other bag'):
        return {}
    return {item[1]: int(item[0]) for item in BAG_RE.findall(data)}


def get_bag(data):
    return {rule[0].strip(): parse_bag(rule[1]) for rule in data}


def check_bag(bag_hash, start, end):
    if not bag_hash.get(start):
        return False

    if end in bag_hash.get(start).keys():
        return True

    for k in bag_hash.get(start):
        if check_bag(bag_hash, k, end):
            return True


def bag_count(bag_hash, start):
    count = 0
    if not bag_hash.get(start):
        return count

    for k in bag_hash.get(start):
        count += bag_hash.get(start).get(k)
        count += bag_hash.get(start).get(k) * bag_count(bag_hash, k)
    return count


def main():
    data = get_data('day7.txt')
    bag_hash = get_bag(data)
    count = sum(1 for bag in bag_hash if check_bag(bag_hash, bag, 'shiny gold'))
    print(f'PART 1: {count}')
    print(f'PART 2: {bag_count(bag_hash, "shiny gold")}')
    # print(bag_hash)


if __name__ == "__main__":
    main()
