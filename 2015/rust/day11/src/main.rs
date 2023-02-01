#[macro_use]
extern crate lazy_static;
use fancy_regex::Regex;

lazy_static! {
    static ref CHECK1: Regex = Regex::new(r"[iol]").unwrap();
    static ref CHECK2: Regex = Regex::new(r"(.)\1.*((?!\1).)\2").unwrap();
}

fn check(input: &str) -> bool {
    !CHECK1.is_match(input).unwrap() && CHECK2.is_match(input).unwrap()
}

fn check_incr(input: &str) -> bool {
    for item in input.as_bytes().windows(3) {
        if item[1] == item[0] + 1 && item[2] == item[1] + 1 {
            return true;
        }
    }
    false
}

fn next_password(input: String) -> String {
    unsafe {
        let mut data = input.into_bytes();
        data.reverse();
        for idx in 0..data.len() {
            if data[idx] < 122 {
                data[idx] += 1;
                break;
            }
            data[idx] = 97;
        }
        data.reverse();
        String::from_utf8_unchecked(data)
    }
}

fn solve(input: &str) -> String {
    let mut current = input.to_string();
    loop {
        let candidate = next_password(current);
        if check(&candidate) && check_incr(&candidate) {
            return candidate;
        }
        current = candidate;
    }
}

fn main() {
    let data = include_str!("input.txt").trim();
    let part1 = solve(data);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", solve(&part1));
}
