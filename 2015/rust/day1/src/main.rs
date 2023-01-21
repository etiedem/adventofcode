fn main() {
    let data = include_str!("input.txt").trim();
    let mut floor = 0;
    let mut basement = 0;
    for (idx, c) in data.chars().enumerate() {
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => unreachable!("Unexpected character: {}", c),
        }
        if floor == -1 && basement == 0 {
            basement = idx + 1;
        }
    }
    println!("Part 1: {}", floor);
    println!("Part 2: {}", basement);
}
