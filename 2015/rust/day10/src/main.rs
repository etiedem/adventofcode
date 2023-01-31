#[macro_use]
extern crate lazy_static;

use fancy_regex::Regex;

fn lookandsay(input: &str) -> String {
    lazy_static! {
        static ref ITEM: Regex = Regex::new(r"((.)(\2)+)|(.)").unwrap();
    }
    let mut output = String::new();
    for capture in ITEM.captures_iter(input) {
        if let Some(item) = capture.unwrap().get(0) {
            output.extend([
                item.as_str().len().to_string(),
                item.as_str().chars().last().unwrap().to_string(),
            ])
        }
    }
    output
}

fn repeat(input: &str, number: u16) -> String {
    let mut current = input.to_string();
    for _ in 0..number {
        let output = lookandsay(&current);
        current = output;
    }
    current
}

fn main() {
    let data = include_str!("input.txt").trim();
    println!("Part 1: {:#?}", repeat(data, 40).len());
    println!("Part 2: {:#?}", repeat(data, 50).len());
}
