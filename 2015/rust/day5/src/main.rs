#[macro_use]
extern crate lazy_static;
use fancy_regex::Regex;

fn is_nice(data: &str) -> bool {
    lazy_static! {
        static ref CHECK1: Regex = Regex::new(r"([aeiou].*){3,}").unwrap();
        static ref CHECK2: Regex = Regex::new(r"(.)\1").unwrap();
        static ref CHECK3: Regex = Regex::new(r"ab|cd|pq|xy").unwrap();
    }
    if CHECK1.is_match(data).unwrap()
        && CHECK2.is_match(data).unwrap()
        && !CHECK3.is_match(data).unwrap()
    {
        return true;
    }
    false
}

fn is_nice2(data: &str) -> bool {
    lazy_static! {
        static ref CHECK1: Regex = Regex::new(r"(..).*\1").unwrap();
        static ref CHECK2: Regex = Regex::new(r"(.).\1").unwrap();
    }
    if CHECK1.is_match(data).unwrap() && CHECK2.is_match(data).unwrap() {
        return true;
    }
    false
}

fn main() {
    let data = include_str!("input.txt").trim();
    let part1 = data.lines().filter(|line| is_nice(line)).count();
    let part2 = data.lines().filter(|line| is_nice2(line)).count();
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
