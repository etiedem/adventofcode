fn find_md5(data: &str, num: usize, mut code: i32) -> i32 {
    loop {
        let digest = format!("{:x}", md5::compute(format!("{}{}", data, code)));
        if digest.starts_with(format!("{:0num$}", 0).as_str()) {
            break;
        }
        code += 1;
    }
    code
}

fn main() {
    let data = include_str!("input.txt").trim();
    let part1 = find_md5(data, 5, 0);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", find_md5(data, 6, part1));
}
