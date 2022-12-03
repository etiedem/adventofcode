use std::fs::File;
use std::io::Read;
use std::collections::HashMap;
use lazy_static::lazy_static;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum CHOICE {
    ROCK = 1,
    PAPER = 2,
    SCISSORS = 3,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum RESULT {
    WIN = 6,
    DRAW = 3,
    LOSE = 0,
}

lazy_static! {
    static ref RPS_HASH: HashMap<&'static str, CHOICE> = HashMap::from([
        ("A", CHOICE::ROCK),
        ("B", CHOICE::PAPER),
        ("C", CHOICE::SCISSORS),
        ("X", CHOICE::ROCK),
        ("Y", CHOICE::PAPER),
        ("Z", CHOICE::SCISSORS),
    ]);
}

lazy_static! {
    static ref RPS_RESULT_HASH: HashMap<&'static str, RESULT> = HashMap::from([
        ("X", RESULT::LOSE),
        ("Y", RESULT::DRAW),
        ("Z", RESULT::WIN),
    ]);
}

fn get_data(filename: &str) -> String {
    let mut file = File::open(filename).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn parse_data(data: String) -> Vec<Vec<String>> {
    data.lines().map(|x| x.split_whitespace().map(|x| x.to_string()).collect()).collect()
}

fn check_game(player1: &String, player2: &String) -> u32 {
    let p1 = RPS_HASH.get(player1.as_str()).unwrap();
    let p2 = RPS_HASH.get(player2.as_str()).unwrap();

    if p1 == p2 { return RESULT::DRAW as u32 + *p2 as u32 }
    match (p1, p2) {
        (CHOICE::SCISSORS, CHOICE::ROCK) => return RESULT::WIN as u32 + *p2 as u32,
        (CHOICE::ROCK, CHOICE::PAPER) => return RESULT::WIN as u32 + *p2 as u32,
        (CHOICE::PAPER, CHOICE::SCISSORS) => return RESULT::WIN as u32 + *p2 as u32,
        _ => return RESULT::LOSE as u32 + *p2 as u32,
    }
}

fn set_game(player1: &String, result: &String) -> u32 {
    let p1 = RPS_HASH.get(player1.as_str()).unwrap();
    let r  = RPS_RESULT_HASH.get(result.as_str()).unwrap();

    match r {
        RESULT::WIN => {
            match p1 {
                CHOICE::ROCK =>     return *r as u32 + CHOICE::PAPER as u32,
                CHOICE::PAPER =>    return *r as u32 + CHOICE::SCISSORS as u32,
                CHOICE::SCISSORS => return *r as u32 + CHOICE::ROCK as u32,
            }
        },
        RESULT::LOSE => {
            match p1 {
                CHOICE::ROCK =>     return *r as u32 + CHOICE::SCISSORS as u32,
                CHOICE::PAPER =>    return *r as u32 + CHOICE::ROCK as u32,
                CHOICE::SCISSORS => return *r as u32 + CHOICE::PAPER as u32,
            }
        },
        _ => return *r as u32 + *p1 as u32,
    }
}
fn main() {
    let data = parse_data(get_data("data.txt"));
    println!("PART1: {:?}", data.iter().map(|x| check_game(&x[0], &x[1])).sum::<u32>());
    println!("PART2: {:?}", data.iter().map(|x| set_game(&x[0], &x[1])).sum::<u32>());
}
