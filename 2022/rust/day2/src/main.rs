use lazy_static::lazy_static;
use std::collections::HashMap;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Choice {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Result {
    Win = 6,
    Draw = 3,
    Lose = 0,
}

lazy_static! {
    static ref RPS_HASH: HashMap<char, Choice> = HashMap::from([
        ('A', Choice::Rock),
        ('B', Choice::Paper),
        ('C', Choice::Scissors),
        ('X', Choice::Rock),
        ('Y', Choice::Paper),
        ('Z', Choice::Scissors),
    ]);
}

lazy_static! {
    static ref RPS_RESULT_HASH: HashMap<char, Result> =
        HashMap::from([('X', Result::Lose), ('Y', Result::Draw), ('Z', Result::Win),]);
}

fn parse_data(data: &str) -> Vec<Vec<char>> {
    data.lines()
        .map(|x| x.split_whitespace().map(|c| c.parse().unwrap()).collect())
        .collect()
}

fn check_game(player1: &char, player2: &char) -> u32 {
    let p1 = RPS_HASH.get(player1).unwrap();
    let p2 = RPS_HASH.get(player2).unwrap();

    if p1 == p2 {
        return Result::Draw as u32 + *p2 as u32;
    }
    match (p1, p2) {
        (Choice::Scissors, Choice::Rock) => Result::Win as u32 + *p2 as u32,
        (Choice::Rock, Choice::Paper) => Result::Win as u32 + *p2 as u32,
        (Choice::Paper, Choice::Scissors) => Result::Win as u32 + *p2 as u32,
        _ => Result::Lose as u32 + *p2 as u32,
    }
}

fn set_game(player1: &char, result: &char) -> u32 {
    let p1 = RPS_HASH.get(player1).unwrap();
    let r = RPS_RESULT_HASH.get(result).unwrap();

    match r {
        Result::Win => match p1 {
            Choice::Rock => *r as u32 + Choice::Paper as u32,
            Choice::Paper => *r as u32 + Choice::Scissors as u32,
            Choice::Scissors => *r as u32 + Choice::Rock as u32,
        },
        Result::Lose => match p1 {
            Choice::Rock => *r as u32 + Choice::Scissors as u32,
            Choice::Paper => *r as u32 + Choice::Rock as u32,
            Choice::Scissors => *r as u32 + Choice::Paper as u32,
        },
        _ => *r as u32 + *p1 as u32,
    }
}
fn main() {
    let data = parse_data(include_str!("data.txt"));
    println!(
        "PART1: {:?}",
        data.iter().map(|x| check_game(&x[0], &x[1])).sum::<u32>()
    );
    println!(
        "PART2: {:?}",
        data.iter().map(|x| set_game(&x[0], &x[1])).sum::<u32>()
    );
}
