use std::fs;
use std::str::FromStr;
use std::string::ParseError;

#[derive(Debug)]
struct Instruction {
    direction: String,
    step: i64
}

impl FromStr for Instruction {
    type Err = ParseError;
    fn from_str(s: &str) -> Result<Self,Self::Err> {
        let data: Vec<String> = s.split_whitespace().map(|s| s.to_string()).collect();
        Ok(Instruction {
            direction: data[0].to_string(),
            step: data[1].parse().unwrap()
        })
    }
}

fn get_data(filename: &str) -> Vec<Instruction> {
    let contents = fs::read_to_string(filename).expect("Error reading file");
    let data: Vec<Instruction> = contents.trim()
    .split("\n")
    .map(|s| s.parse().unwrap())
    .collect();
    data
}

fn part1(data: &Vec<Instruction>) -> i64 {
    let mut x = 0;
    let mut y = 0;
    for i in data {
        match i.direction.as_str() {
            "forward" => x += i.step,
            "up" => y -= i.step,
            "down" => y += i.step,
            _ => panic!("Invalid direction"),
        }
    }
    x * y
}

fn part2(data: &Vec<Instruction>) -> i64 {
    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;
    for i in data {
        match i.direction.as_str() {
            "forward" => {x += i.step; y += i.step * aim;}
            "up" => aim -= i.step,
            "down" => aim += i.step,
            _ => panic!("Invalid direction"),
        }
    }
    x * y
}

fn main() {
    let data = get_data("src/input.txt");

    println!("PART 1: {}", part1(&data));
    println!("PART 2: {}", part2(&data));
}
