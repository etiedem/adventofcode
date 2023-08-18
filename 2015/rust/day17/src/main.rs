use itertools::Itertools;

fn find_combinations(containers: &[i32], total: i32, limit: usize) -> Vec<Vec<i32>> {
    let count = 1;
    let mut output = Vec::new();
    for idx in count..limit {
        for num in containers.iter().combinations(idx) {
            let num: Vec<i32> = num.iter().map(|&x| *x).collect();
            if num.iter().sum::<i32>() == total {
                output.push(num);
            }
        }
    }
    output
}

fn main() {
    let mut containers: Vec<i32> = include_str!("input.txt")
        .lines()
        .filter_map(|x| str::parse(x).ok())
        .collect();
    containers.sort();

    let p1 = find_combinations(&containers, 150, containers.len());
    println!("Part 1: {}", p1.len());

    let min_containers = p1.iter().min_by_key(|x| x.len()).unwrap().len();
    let p2 = p1.iter().filter(|x| x.len() == min_containers).count();
    println!("Part 2: {}", p2);
}
