use itertools::Itertools;
use phf::phf_map;

static KEY: phf::Map<&'static str, usize> = phf_map! {
    "Faerun" => 0,
    "Norrath" => 1,
    "Tristram" => 2,
    "AlphaCentauri" => 3,
    "Arbre" => 4,
    "Snowdin" => 5,
    "Tambi" => 6,
    "Straylight" => 7,
};

fn create_adjacency_matrix(input: &str) -> [[i32; 8]; 8] {
    let mut matrix = [[0i32; 8]; 8];
    for line in input.lines() {
        let mut data = line.split_whitespace().step_by(2);
        let x = KEY.get(data.next().unwrap()).unwrap();
        let y = KEY.get(data.next().unwrap()).unwrap();
        let dist = data.next().unwrap();
        matrix[*y][*x] = dist.parse().unwrap();
        matrix[*x][*y] = dist.parse().unwrap();
    }
    matrix
}

fn multiply_by_negative(matrix: [[i32; 8]; 8]) -> [[i32; 8]; 8] {
    let mut new = [[0i32; 8]; 8];
    for y in 0..matrix.len() {
        for x in 0..matrix[0].len() {
            new[y][x] = -matrix[y][x];
        }
    }
    new
}

fn path_to_city(path: Vec<usize>) -> Vec<String> {
    let mut output = vec![];
    let key: Vec<String> = KEY
        .into_iter()
        .sorted_by_key(|x| x.1)
        .map(|(key, _)| key.to_string())
        .collect();
    for p in path {
        output.push(key[p].clone());
    }
    output
}

fn shortest(matrix: [[i32; 8]; 8], path: &[&&usize]) -> i32 {
    let mut result = 0;
    let mut current = path[0];
    for p in path.iter().skip(1) {
        result += matrix[**current][***p];
        current = *p;
    }
    result
}

fn solve(matrix: [[i32; 8]; 8], options: &[&usize]) -> (i32, Vec<usize>) {
    let mut short = i32::MAX;
    let mut s_path: Vec<usize> = Vec::new();
    for path in options.iter().permutations(8) {
        let candidate = shortest(matrix, &path);
        if candidate < short {
            short = candidate;
            s_path = path.iter().map(|x| *(**x)).collect();
        }
    }
    (short, s_path)
}

fn main() {
    let data = include_str!("input.txt").trim();
    let adjacency = create_adjacency_matrix(data);
    let path = KEY.values().collect_vec();
    let (s_dist, s_path) = solve(adjacency, &path);
    let (mut l_dist, l_path) = solve(multiply_by_negative(adjacency), &path);
    l_dist *= -1;
    println!("Part 1: {:#?}", s_dist);
    println!("Part 1: {:#?}", path_to_city(s_path));
    println!("Part 2: {:#?}", l_dist);
    println!("Part 2: {:#?}", path_to_city(l_path));
}
