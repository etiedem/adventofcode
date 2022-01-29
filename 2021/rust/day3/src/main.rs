use std::fs;
use counter::Counter;

fn get_data(filename: &str) -> Vec<String> {
    let contents = fs::read_to_string(filename).expect("Error reading file");
    contents.split_whitespace()
        .map(|s| s.parse::<String>().unwrap())
        .collect()
}

fn get_column(data: &Vec<String>, column: usize) -> String {
    data.iter()
        .map(|s| s.as_bytes()[column] as char)
        .collect()
}

fn most_least_common(data: &String) -> Vec<(char, usize)> {
    data.chars().collect::<Counter<_>>().most_common_ordered()
}

fn part1(data: &Vec<String>) -> isize {
    let mut gamma = String::new();
    let mut epsilon = String::new();

    for x in 0..data[0].len() {
        let counts = most_least_common(&get_column(&data, x));
        gamma.push(counts[0].0);
        epsilon.push(counts[1].0);
    }
    isize::from_str_radix(&gamma, 2).unwrap() * isize::from_str_radix(&epsilon, 2).unwrap()
}

fn part2(data: &Vec<String>) -> isize {
    let mut oxygen = data.to_vec();
    for x in 0..data[0].chars().count() {
        if oxygen.len() < 2 { break }
        let mut counts = most_least_common(&get_column(&oxygen, x));
        if counts.len() > 1 && counts[0].1 == counts[1].1 {
            counts[0].0 = '1';
        }
        oxygen.retain(|s| s.chars().nth(x) == Some(counts[0].0));
    }

    let mut co2 = data.to_vec();
    for x in 0..data[0].chars().count() {
        if co2.len() < 2 { break }
        let mut counts = most_least_common(&get_column(&co2, x));
        if counts.len() > 1 && counts[0].1 == counts[1].1 {
            counts[1].0 = '0';
        }
        co2.retain(|s| s.chars().nth(x) == Some(counts[1].0));
    }

    isize::from_str_radix(&oxygen[0], 2).unwrap() * isize::from_str_radix(&co2[0], 2).unwrap()
}

fn main() {
    let data = get_data("src/input.txt");
    println!("PART 1: {}", part1(&data));
    println!("PART 2: {:?}", part2(&data));
}
