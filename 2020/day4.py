from rich import print


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [{x[0]: x[1]
                 for item in line.split()
                 if (x := item.split(":"))}
                for line in f.read().split("\n\n")]


def is_valid(passport):
    check = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    if len(check - passport.keys()) != 0:
        return False

    return birth(passport["byr"]) and issue(passport["iyr"]) and expiration(
        passport["eyr"]
    ) and height(passport["hgt"]) and hcl(passport["hcl"]) and eye(
        passport["ecl"]
    ) and pid(passport["pid"])


def birth(data):
    return len(data) == 4 and 1920 <= int(data) <= 2002


def issue(data):
    return len(data) == 4 and 2010 <= int(data) <= 2020


def expiration(data):
    return len(data) == 4 and 2020 <= int(data) <= 2030


def height(data):
    num = data[:-2]
    typ = data[-2:]

    if typ == "cm":
        return 150 <= int(num) <= 193

    if typ == "in":
        return 59 <= int(num) <= 76

    return False


def hcl(data):
    check = {
        "a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    }
    return len(data) == 7 and data[0] == "#" and all(x in check for x in data[1:])


def eye(data):
    eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return data in eyes


def pid(data):
    return len(data) == 9 and data.isnumeric()


def main():
    data = get_data("day4.txt")
    count = sum(1 for passport in data if is_valid(passport))
    print(count)


if __name__ == "__main__":
    main()
