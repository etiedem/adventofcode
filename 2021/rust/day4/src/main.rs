use std::fs;

fn get_data(filename: &str) -> (Vec<u32>, Vec<Vec<Vec<u32>>>) {
    let data = fs::read_to_string(filename).expect("Error reading file");
    let breaks: Vec<String> = data.split("\n\n")
        .map(|s| s.trim().parse::<String>().unwrap())
        .collect();
    let calls: Vec<u32> = breaks[0].split(",")
        .map(|c| c.parse::<u32>().unwrap())
        .collect();
    let cards: Vec<Vec<Vec<u32>>> = breaks[1..breaks.len()].iter()
        .map(|card| card.split("\n")
            .map(|line| line.split_whitespace()
                .map(|item| item.parse::<u32>().unwrap())
                .collect()
            ).collect()
        ).collect();
    (calls, cards)
}

fn main() {
    let data = get_data("src/input.txt");
    dbg!(data);
}
