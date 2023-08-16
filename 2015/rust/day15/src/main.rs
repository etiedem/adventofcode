use itertools::{any, iproduct};
use std::collections::HashMap;
use std::iter::zip;
use std::vec;

struct Ingredient {
    name: String,
    capacity: i32,
    durability: i32,
    flavor: i32,
    texture: i32,
    calories: i32,
}

impl From<&str> for Ingredient {
    fn from(value: &str) -> Self {
        let value = value.replace(',', "");
        let mut parts = value.split_whitespace().step_by(2);
        Ingredient {
            name: parts.next().unwrap().to_string(),
            capacity: parts.next().unwrap().parse().unwrap(),
            durability: parts.next().unwrap().parse().unwrap(),
            flavor: parts.next().unwrap().parse().unwrap(),
            texture: parts.next().unwrap().parse().unwrap(),
            calories: parts.next().unwrap().parse().unwrap(),
        }
    }
}

fn find_best(ingredient: &HashMap<String, Ingredient>, num: i32, cal: bool) -> i32 {
    let mut max_score = i32::MIN;
    let i = ingredient.keys();
    for (a, b, c) in iproduct!(0..num, 0..num, 0..num) {
        let new_num = num - (a + b + c);
        if num - new_num < 0 {
            continue;
        }
        let new_num = vec![a, b, c, new_num];
        let score = calc_score(ingredient, zip(i.clone(), new_num).collect(), cal);
        max_score = max_score.max(score);
    }
    max_score
}

fn calc_score(
    ingredient: &HashMap<String, Ingredient>,
    amounts: Vec<(&String, i32)>,
    cal: bool,
) -> i32 {
    let (mut total_cap, mut total_dur, mut total_flav) = (0, 0, 0);
    let (mut total_text, mut total_cal) = (0, 0);
    let max_calories = 500;

    for amount in amounts {
        let (name, num) = amount;
        total_cap += ingredient.get(name).unwrap().capacity * num;
        total_dur += ingredient.get(name).unwrap().durability * num;
        total_flav += ingredient.get(name).unwrap().flavor * num;
        total_text += ingredient.get(name).unwrap().texture * num;
        total_cal += ingredient.get(name).unwrap().calories * num;
    }
    let all = vec![total_cap, total_dur, total_flav, total_text];
    if any(all, |x| x < 1) {
        return 0;
    }

    if cal && total_cal != max_calories {
        return 0;
    }
    total_cap * total_dur * total_flav * total_text
}

fn main() {
    let data = include_str!("input.txt");
    let ingredients: HashMap<String, _> = data
        .lines()
        .map(|line| {
            let i = Ingredient::from(line);
            (i.name.to_owned(), i)
        })
        .collect();

    let p1 = find_best(&ingredients, 100, false);
    println!("Part 1: {}", p1);

    let p2 = find_best(&ingredients, 100, true);
    println!("Part 2: {}", p2);
}
