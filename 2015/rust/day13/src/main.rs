use itertools::Itertools;
use std::collections::{HashMap, HashSet};

fn create_keys(d: &str) -> (HashMap<String, usize>, HashMap<String, usize>) {
    let mut keys = HashSet::new();
    for line in d.lines() {
        let words: Vec<_> = line.split_whitespace().collect();
        keys.insert(words[0].to_owned());
        keys.insert(words[words.len() - 1].trim_end_matches('.').to_owned());
    }
    let p1_keys: HashMap<String, usize> = keys
        .iter()
        .enumerate()
        .map(|(i, k)| (k.to_owned(), i))
        .collect();
    keys.insert("Self".to_owned());
    let p2_keys: HashMap<String, usize> = keys
        .iter()
        .enumerate()
        .map(|(i, k)| (k.to_owned(), i))
        .collect();
    (p1_keys, p2_keys)
}

fn create_adjacency_matrix(data: &str, keys: HashMap<String, usize>) -> Vec<Vec<i32>> {
    let mut matrix = vec![vec!(0i32; keys.len()); keys.len()];
    for line in data.lines() {
        let words: Vec<_> = line.split_whitespace().collect();
        let from = keys[words[0]];
        let to = keys[words[words.len() - 1].trim_end_matches('.')];
        let gain_loss = words[2];
        let happy = words[3].parse::<i32>().unwrap();
        match gain_loss {
            "gain" => matrix[from][to] = happy,
            "lose" => matrix[from][to] = -happy,
            _ => panic!("Unknown gain/loss: {}", gain_loss),
        }
    }
    matrix
}

fn solve(matrix: Vec<Vec<i32>>, options: Vec<&usize>) -> i32 {
    let mut short = -i32::MAX;
    for path in options.iter().permutations(options.len()) {
        let candidate = score(&matrix, path);
        if candidate > short {
            short = candidate;
        }
    }
    short
}

fn score(matrix: &[Vec<i32>], path: Vec<&&usize>) -> i32 {
    let mut total = 0;
    for i in 0..path.len() - 1 {
        total += matrix[**path[i]][**path[i + 1]];
        total += matrix[**path[i + 1]][**path[i]];
    }
    total += matrix[**path[0]][**path[path.len() - 1]];
    total += matrix[**path[path.len() - 1]][**path[0]];
    total
}

fn main() {
    let data = include_str!("input.txt").trim();
    let (p1_keys, p2_keys) = create_keys(data);

    let matrix = create_adjacency_matrix(data, p1_keys.clone());
    let p1 = solve(matrix, p1_keys.values().collect_vec());
    println!("Part 1: {}", p1);

    let matrix = create_adjacency_matrix(data, p2_keys.clone());
    let p2 = solve(matrix, p2_keys.values().collect_vec());
    println!("Part 2: {}", p2);
}
