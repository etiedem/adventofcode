use std::fs::File;
use std::io::Read;
use std::collections::HashSet;

fn get_data(filename: &str) -> String {
    let mut file = File::open(filename).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn parse_data_part1(data: String) -> Vec<(HashSet<char>, HashSet<char>)> {
    let mut result = Vec::new();
    for d in data.lines() {
        let div = d.len() / 2;
        let front: HashSet<char> = HashSet::from_iter(d[..div].chars());
        let back: HashSet<char> = HashSet::from_iter(d[div..].chars());
        result.push((front, back));
    }
    result
}

fn parse_data_part2(data: String) -> Vec<(HashSet<char>, HashSet<char>, HashSet<char>)> {
    let mut result = Vec::new();
    let mut lines = data.lines();
    while let (Some(a), Some(b), Some(c)) = (lines.next(), lines.next(), lines.next()) {
        let front: HashSet<char> = HashSet::from_iter(a.chars());
        let middle: HashSet<char> = HashSet::from_iter(b.chars());
        let back: HashSet<char> = HashSet::from_iter(c.chars());
        result.push((front, middle, back));
    }
    result
}

fn get_value(c: char) -> u32 {
    let mut alpha = (b'a'..=b'z').map(char::from).collect::<Vec<char>>();
    alpha.extend((b'A'..=b'Z').map(char::from).collect::<Vec<char>>());
    alpha.iter().position(|&x| x == c).unwrap() as u32 + 1
}

fn part1(data: Vec<(HashSet<char>, HashSet<char>)>) -> u32 {
    data
    .iter()
    .map(|x|
        x.0.intersection(&x.1)
        .map(|x| get_value(*x))
        .sum::<u32>()
    ).sum()
}

fn part2(data: Vec<(HashSet<char>, HashSet<char>, HashSet<char>)>) -> u32 {
    data
    .iter()
    .map(|x|
        x.0.intersection(&x.1).copied().collect::<HashSet<char>>()
        .intersection(&x.2).copied()
        .map(|x| get_value(x))
        .sum::<u32>()
    ).sum()
}

fn main() {
    let data_part1 = parse_data_part1(get_data("data.txt"));
    println!("PART1: {:?}", part1(data_part1));

    let data_part2 = parse_data_part2(get_data("data.txt"));
    println!("PART2: {:?}", part2(data_part2));
}
