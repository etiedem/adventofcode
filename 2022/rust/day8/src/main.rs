fn parse_data(data: &str) -> (usize, Vec<u32>) {
    let lines = data
            .lines();
    let length = lines.clone().next().unwrap().len();
    let puzzle = lines
            .flat_map(|line| line
                .chars()
                .filter_map(|c| c.to_digit(10))
            ).collect();
    (length, puzzle)
}

fn idx_is_highest((idx, data): &(usize, Vec<u32>)) -> bool {
    if data[..*idx].iter().max() < Some(&data[*idx]) { return true }
    if data[idx+1..].iter().max() < Some(&data[*idx]) { return true }
    false
}

fn get_row(idx: usize, length: usize, data: &[u32]) -> (usize, Vec<u32>) {
    let start = idx - (idx % length);
    let row = data[start ..(start + length)].to_vec();
    (idx%length, row)
}

fn get_column(idx: usize, length: usize, data: &[u32]) -> (usize, Vec<u32>) {
    let skip = idx % length;
    let column: Vec<u32> = data.iter().skip(skip).step_by(length).cloned().collect();
    (idx/length, column)
}

fn find_all_visible(length: usize, data: &[u32]) -> usize {
    data.iter()
        .enumerate()
        .filter(|(idx, _)| {
            if idx % length == 0 { return true } // first column is visible
            if idx % length == length-1 { return true } // last column is visible
            if *idx < length { return true } // All first row is visible
            if idx + length > data.iter().len() { return true } // Last row is visible
            if idx_is_highest(&get_row(*idx, length, data)) { return true }
            if idx_is_highest(&get_column(*idx, length, data)) { return true }
            false
        }).count()
}

fn how_far((idx, data): &(usize, Vec<u32>)) -> u32 {
    let mut top = 0;
    for i in (0..*idx).rev() {
        if data[i] < data[*idx] { top += 1 } else { top += 1; break }
    }
    let mut bottom = 0;
    for i in idx+1..data.len() {
        if data[i] < data[*idx] { bottom += 1 } else { bottom += 1; break }
    }
    top * bottom
}

fn most_scenic(length: usize, data: &[u32]) -> u32 {
    data.iter()
        .enumerate()
        .map(
            |(idx, _)| {
                how_far(&get_column(idx, length, data)) *
                how_far(&get_row(idx, length, data))
            }
        ).max().unwrap()
}

fn main() {
    let (length, data) = parse_data(include_str!("data.txt"));
    println!("Part 1: {}", find_all_visible(length, &data));
    println!("Part 2: {}", most_scenic(length, &data));
}
