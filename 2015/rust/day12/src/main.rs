use regex::Regex;
use serde_json::Value;

fn get_numbers(input: &str) -> i32 {
    let match_num = Regex::new(r"(-?\d+)").unwrap();
    match_num
        .captures_iter(input)
        .map(|x| x.get(1).unwrap().as_str().parse::<i32>().unwrap())
        .sum()
}

fn get_sum(obj: Value) -> i64 {
    let mut sum = 0;

    if obj.is_array() {
        let ary = obj.as_array().unwrap();
        for value in ary.iter() {
            if value.is_number() {
                sum += value.as_i64().unwrap();
            } else if value.is_array() {
                sum += get_sum(value.clone());
            } else if value.is_object() {
                sum += get_sum(value.clone());
            }
        }
    }

    if obj.is_object() {
        let hash = obj.as_object().unwrap();
        if hash.keys().any(|x| x == "red") || hash.values().any(|x| x == "red") {
            return 0;
        }
        for (_, value) in hash {
            if value.is_number() {
                sum += value.as_i64().unwrap();
            } else if value.is_array() {
                sum += get_sum(value.clone());
            } else if value.is_object() {
                sum += get_sum(value.clone());
            }
        }
    }
    sum
}

fn main() {
    let data = include_str!("input.txt").trim();
    println!("Part 1: {:#?}", get_numbers(data));
    let data_p2: Value = serde_json::from_str(data).unwrap();
    println!("Part 2: {:#?}", get_sum(data_p2));
}
