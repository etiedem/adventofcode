#!/usr/bin/env python3.11

import pathlib

import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = pathlib.Path(__file__).parent


def get_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookie = httpx.Cookies({"session": (BASE_DIR / "session.txt").read_text().strip()})
    return httpx.Client(cookies=cookie).get(url).text.strip()


def main(year: int, day: int):
    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    python_template = env.get_template("py_template.j2")
    py_test_template = env.get_template("py_test_template.j2")

    year_dir = BASE_DIR / str(year) / "python"
    if not year_dir.exists():
        year_dir.mkdir()

    day_pad = f"{day:02d}"
    day_dir = year_dir / f"day{day_pad}"
    if not day_dir.exists():
        day_dir.mkdir()

    day_file = day_dir / f"day{day_pad}.py"
    if not day_file.exists():
        with open(day_file, "w") as f:
            f.write(python_template.render(day=day_pad))
        day_file.chmod(0o755)
    else:
        print("Day file already exists.")

    test_file = day_dir / f"test_day{day_pad}.py"
    if not test_file.exists():
        with open(test_file, "w") as f:
            f.write(py_test_template.render(day=day_pad))
    else:
        print("Test file already exists.")

    input_file = day_dir / f"day{day_pad}.txt"
    if not input_file.exists():
        with open(input_file, "w") as f:
            f.write(get_input(year, day))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    main(args.year, args.day)
