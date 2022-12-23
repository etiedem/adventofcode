use std::collections::HashSet;

fn parse_data_part1(data: &str) -> Vec<(HashSet<char>, HashSet<char>)> {
    data.lines()
        .map(|line| line.split_at(line.len() / 2))
        .map(|(a, b)| (HashSet::from_iter(a.chars()), HashSet::from_iter(b.chars())))
        .collect()
}

fn parse_data_part2(data: &str) -> Vec<(HashSet<char>, HashSet<char>, HashSet<char>)> {
    let mut result = Vec::new();
    for elves in data.split_whitespace().collect::<Vec<_>>().chunks(3) {
        result.push((
            HashSet::from_iter(elves[0].chars()),
            HashSet::from_iter(elves[1].chars()),
            HashSet::from_iter(elves[2].chars()),
        ))
    }
    result
}

fn get_value(c: char) -> u32 {
    let mut alpha: Vec<char> = (b'a'..=b'z').map(char::from).collect();
    alpha.extend((b'A'..=b'Z').map(char::from).collect::<Vec<char>>());
    alpha.iter().position(|&x| x == c).unwrap() as u32 + 1
}

fn part1(data: Vec<(HashSet<char>, HashSet<char>)>) -> u32 {
    data.iter()
        .map(|x| x.0.intersection(&x.1).map(|x| get_value(*x)).sum::<u32>())
        .sum()
}

fn part2(data: Vec<(HashSet<char>, HashSet<char>, HashSet<char>)>) -> u32 {
    data.iter()
        .map(|x| {
            x.0.intersection(&x.1)
                .copied()
                .collect::<HashSet<char>>()
                .intersection(&x.2)
                .copied()
                .map(get_value)
                .sum::<u32>()
        })
        .sum()
}

fn main() {
    let data_part1 = parse_data_part1(include_str!("data.txt"));
    println!("PART1: {:?}", part1(data_part1));

    let data_part2 = parse_data_part2(include_str!("data.txt"));
    println!("PART2: {:?}", part2(data_part2));
}
