use std::fs;

fn get_data(path: &str) -> Vec<i64> {
    let contents = fs::read_to_string(path).expect("Error reading file");
    let data: Vec<i64> = contents.split_whitespace().map(|s| s.parse::<i64>().unwrap()).collect();
    data
}

fn day1(data: &Vec<i64>) {
    let mut count = 0;
    for x in data.windows(2) {
        if x[0] < x[1] {
            count += 1;
        }
    }
    println!("DAY 1: {}", count);
}

fn day2(data: &Vec<i64>) {
    let mut count = 0;
    let window1 = data.windows(3);
    let window2 = data[1..].windows(3);
    for windows in window1.zip(window2) {
        let (w1, w2) = windows;
        if w1.iter().sum::<i64>() < w2.iter().sum() {
            count += 1;
        }
    }
    println!("DAY 2: {}", count);
}

fn main() {
    let data = get_data("src/input.txt");
    day1(&data);
    day2(&data);
}
