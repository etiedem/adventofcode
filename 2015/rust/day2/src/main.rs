fn main() {
    let data = include_str!("input.txt").trim();

    let mut wrapping_paper: u32 = 0;
    let mut ribbon: u32 = 0;
    for line in data.lines() {
        let mut dims: Vec<u32> = line.split('x').map(|s| s.parse::<u32>().unwrap()).collect();
        let (l, w, h) = (dims[0], dims[1], dims[2]);
        dims.sort();

        wrapping_paper += (2 * l * w) + (2 * w * h) + (2 * h * l) + (dims[0] * dims[1]);
        ribbon += (dims[0] * 2) + (dims[1] * 2) + (l * w * h);
    }

    println!("Part 1: {}", wrapping_paper);
    println!("Part 2: {}", ribbon);
}
