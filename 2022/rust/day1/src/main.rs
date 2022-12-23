fn parse_data(data: &str) -> Vec<Vec<u32>> {
    data.split("\n\n")
        .map(|section| {
            section
                .split_whitespace()
                .map(|n| n.parse().unwrap())
                .collect()
        })
        .collect()
}

fn largest(data: &[Vec<u32>], num: usize) -> u32 {
    let mut calories: Vec<u32> = data.iter().map(|x| x.iter().sum()).collect();
    calories.sort_by(|a, b| b.cmp(a));
    calories.iter().take(num).sum()
}
fn main() {
    let data = parse_data(include_str!("data.txt"));
    println!("PART1: {:?}", largest(&data, 1));
    println!("PART2: {:?}", largest(&data, 3));
}
