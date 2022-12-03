use std::fs::File;
use std::io::Read;
use std::cmp::Reverse;

fn get_data(filename: &str) -> String {
    let mut file = File::open(filename).expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");
    contents
}

fn parse_data(data: String) -> Vec<Vec<u32>> {
    let mut result = Vec::new();
    let mut tmp = Vec::new();
    for line in data.lines() {
        if !line.is_empty() {
           tmp.push(line.parse::<u32>().unwrap());
        } else {
            result.push(tmp);
            tmp = Vec::new();
        }
    }
    result
}

fn largest(data: &Vec<Vec<u32>>, num: usize) -> u32 {
    let mut d = data.clone();
    d.sort_by_key(|x| Reverse(x.iter().sum::<u32>()));
    d[..num].to_vec().iter().map(|x| x.iter().sum::<u32>()).sum::<u32>()
}
fn main() {
    let data = parse_data(get_data("data.txt"));
    println!("PART1: {:?}", largest(&data, 1));
    println!("PART2: {:?}", largest(&data, 3));
}
