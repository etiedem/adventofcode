use std::collections::vec_deque::VecDeque;

fn get_start_of(data: &str, num: u16) -> u16 {
    let mut iter = data.chars();
    let n = num - 1; // collect this number first
    let mut ring: VecDeque<char> = VecDeque::from(iter.by_ref().take(n as usize).collect::<Vec<char>>());
    let mut count = n;
    for x in iter.by_ref() {
        ring.push_back(x);
        count += 1;
        if ring.iter().all(|x| ring.iter().filter(|y| y==&x).count() == 1) {
            break
        }
        ring.pop_front();
    }
    count

}

fn get_start_of_packet(data: &str) -> u16 {
    // first 4 characters that are all different
    get_start_of(data, 4)
}

fn get_start_of_message(data: &str) -> u16 {
    // first 14 characters that are all different
    get_start_of(data, 14)
}
fn main() {
    let data = include_str!("data.txt");
    let start = get_start_of_packet(data);
    let msg = get_start_of_message(data);
    println!("PART1: {}", start);
    println!("PART2: {}", msg);
}
