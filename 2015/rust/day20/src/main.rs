fn part1(num: u32) -> Vec<u32> {
    let num = num / 10;
    let mut houses = vec![0; num as usize];
    for elf in 1..num + 1 {
        for house in (elf..num + 1).step_by(elf as usize) {
            houses[house as usize - 1] += elf * 10;
        }
    }
    houses
}

fn part2(num: u32) -> Vec<u32> {
    let num = num / 10;
    let mut houses = vec![0; num as usize];
    for elf in 1..num + 1 {
        for house in (elf..(num).min(elf * 50) + 1).step_by(elf as usize) {
            houses[house as usize - 1] += elf * 11;
        }
    }
    houses
}
fn main() {
    let data = include_str!("input.txt");
    let num = data.parse().unwrap();

    let p1 = part1(num).iter().position(|x| *x >= num).unwrap() + 1;
    println!("Part 1: {:#?}", p1);

    let p2 = part2(num).iter().position(|x| *x >= num).unwrap() + 1;
    println!("Part 2: {:#?}", p2);
}
