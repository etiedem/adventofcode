#[macro_use]
extern crate lazy_static;

use std::collections::HashMap;

use itertools::Itertools;
use regex::Regex;

#[derive(Debug)]
struct Instr {
    in1: String,
    in2: String,
    op: Action,
}

#[derive(Debug)]
enum Action {
    Set,
    And,
    Or,
    Lshift,
    Rshift,
    Not,
}

impl From<&str> for Action {
    fn from(input: &str) -> Action {
        match input {
            "AND" => Action::And,
            "OR" => Action::Or,
            "LSHIFT" => Action::Lshift,
            "RSHIFT" => Action::Rshift,
            "NOT" => Action::Not,
            _ => Action::Set,
        }
    }
}

impl Action {
    fn execute(&self, a: i32, b: i32) -> i32 {
        match self {
            Action::And => a & b,
            Action::Or => a | b,
            Action::Lshift => a << b,
            Action::Rshift => a >> b,
            Action::Not => !a,
            Action::Set => a,
        }
    }
}

fn parse_instruction(input: &str) -> (String, Instr) {
    lazy_static! {
        static ref ACTION: Regex = Regex::new(r"([[:upper:]]+)").unwrap();
    }
    let (input, key) = input.split_once(" -> ").unwrap();
    let action: Action = ACTION.find(input).map_or("", |m| m.as_str()).into();
    let input = ACTION.replace(input, "");
    let (in1, in2) = match action {
        Action::Set | Action::Not => {
            let in1 = input.trim();
            (in1.to_string(), "".to_string())
        }
        _ => input
            .split_whitespace()
            .map(|s| s.to_string())
            .collect_tuple()
            .unwrap(),
    };

    (
        key.to_string(),
        Instr {
            in1,
            in2,
            op: action,
        },
    )
}

fn solve(
    instructions: &HashMap<String, Instr>,
    letter: String,
    cache: &mut HashMap<String, i32>,
) -> i32 {
    if cache.get(&letter).is_some() {
        return *cache.get(&letter).unwrap();
    }
    let answer = instructions
        .get(&letter)
        .map(|instr| {
            let in1 = instr
                .in1
                .parse::<i32>()
                .unwrap_or_else(|_| solve(instructions, instr.in1.clone(), cache));
            let in2 = instr
                .in2
                .parse::<i32>()
                .unwrap_or_else(|_| solve(instructions, instr.in2.clone(), cache));
            instr.op.execute(in1, in2)
        })
        .unwrap_or(0);
    cache.insert(letter, answer);
    answer
}

fn main() {
    let data = include_str!("input.txt").trim();
    let mut instructions: HashMap<String, Instr> = HashMap::new();
    for line in data.lines() {
        let (key, instr) = parse_instruction(line);
        instructions.insert(key, instr);
    }
    let part1 = solve(&instructions, "a".to_string(), &mut HashMap::new());
    println!("Part 1: {:?}", part1);
    instructions.insert(
        "b".to_string(),
        Instr {
            in1: part1.to_string(),
            in2: "".to_string(),
            op: Action::Set,
        },
    );
    println!(
        "Part 2: {:?}",
        solve(&instructions, "a".to_string(), &mut HashMap::new())
    );
}
