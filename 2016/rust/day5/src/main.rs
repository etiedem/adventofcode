fn solve(input: &str) -> (String, String) {
    let mut count = 0;
    let mut part1 = String::with_capacity(8);
    let mut part2 = Vec::from(['#'; 8]);
    while part1.len() != 8 || part2.contains(&'#') {
        let current = format!("{}{}", &input, &count);
        let digest = format!("{:x}", md5::compute(current));
        if digest.starts_with("00000") {
            if part1.len() < 8 {
                part1.push(digest.chars().nth(5).unwrap());
            }
            let items: Vec<char> = digest.chars().skip(5).take(2).collect();
            if let Some(idx) = items[0].to_digit(10) {
                if idx < 8 && part2[idx as usize] == '#' {
                    part2[idx as usize] = items[1];
                }
            }
        }
        count += 1;
    }
    (part1, part2.iter().collect())
}

fn main() {
    let data = include_str!("input.txt").trim();
    let (part1, part2) = solve(data);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
