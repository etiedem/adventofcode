struct Triangle(i32, i32, i32);

impl From<&str> for Triangle {
    fn from(value: &str) -> Triangle {
        let sides: Vec<i32> = value
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        Triangle(sides[0], sides[1], sides[2])
    }
}

impl Triangle {
    fn valid(&self) -> bool {
        if self.0 + self.1 > self.2 && self.1 + self.2 > self.0 && self.2 + self.0 > self.1 {
            return true;
        }
        false
    }
}
fn main() {
    let data = include_str!("input.txt");
    let part1 = data
        .lines()
        .map(Triangle::from)
        .filter(|x| x.valid())
        .count();
    println!("Part 1: {:#?}", part1);

    let flatten: Vec<i32> = data
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (mut part2, mut idx) = (0, 0);
    while idx < flatten.len() - 6 {
        if Triangle(flatten[idx], flatten[idx + 3], flatten[idx + 6]).valid() {
            part2 += 1;
        }
        idx += 1;
        if idx % 3 == 0 {
            idx += 6;
        }
    }
    println!("Part 2: {:#?}", part2);
}
