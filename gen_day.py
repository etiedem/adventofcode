#!/usr/bin/env python3.12

import pathlib
import subprocess

import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = pathlib.Path(__file__).parent


def get_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session_file = BASE_DIR / "session.txt"
    if session_file.exists():
        cookie = httpx.Cookies(
            {"session": (BASE_DIR / "session.txt").read_text().strip()}
        )
        return httpx.Client(cookies=cookie).get(url).text.strip()
    raise FileExistsError(f"{session_file} doesn't exist")


def create_input_file(args, day_pad, day_dir):
    input_file = day_dir / f"day{day_pad}.txt"
    if not input_file.exists():
        data = get_input(args.year, args.day)
        with open(input_file, "w") as f:
            f.write(data)
            print("Input file created.")


def main(args):
    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

    is_template = True
    is_command = False
    template = env.get_template("py_template.j2")
    test_template = env.get_template("py_test_template.j2")
    year_dir = BASE_DIR / str(args.year) / "python"
    day_pad = f"{args.day:02d}"
    commands = []

    if args.rust:
        is_template = False
        is_command = True
        year_dir = BASE_DIR / str(args.year) / "rust"
        dir = year_dir
        commands = [f"cargo init day{day_pad}"]

    if args.go:
        is_command = True
        year_dir = BASE_DIR / str(args.year) / "go"
        template = env.get_template("go_template.j2")
        test_template = env.get_template("go_test_template.j2")
        commands = [f"go mod init day{day_pad}", "go get github.com/stretchr/testify"]

    day_dir = year_dir / f"day{day_pad}"

    if not args.rust:
        dir = day_dir

    if not day_dir.exists():
        day_dir.mkdir(parents=True)

    day_file = day_dir / f"day{day_pad}.py"

    if args.go:
        day_file = day_dir / "main.go"

    if is_template:
        if not day_file.exists():
            with open(day_file, "w") as f:
                f.write(template.render(day=day_pad))
            day_file.chmod(0o755)
        else:
            print("Day file already exists.")

    test_file = day_dir / f"test_day{day_pad}.py"
    if args.go:
        test_file = day_dir / "main_test.go"
    if is_template:
        if not test_file.exists():
            with open(test_file, "w") as f:
                f.write(test_template.render(day=day_pad))
        else:
            print("Test file already exists.")

    if is_command:
        for command in commands:
            print(dir)
            subprocess.run(command, cwd=dir, shell=True, check=False)

    create_input_file(args, day_pad, day_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--rust", action="store_true")
    parser.add_argument("--go", action="store_true")
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    main(parser.parse_args())
