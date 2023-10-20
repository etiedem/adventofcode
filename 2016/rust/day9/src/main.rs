fn decompress(input: &str, recurse: bool) -> usize {
    let mut idx = 0;
    let mut length = 0;
    let mut capture: Vec<char> = vec![];
    let mut FLAG: bool = false;

    let data: Vec<_> = input.chars().collect();

    while idx < data.len() {
        if *data.get(idx).unwrap() == ')' {
            let cap: Vec<usize> = capture
                .iter()
                .collect::<String>()
                .split('x')
                .map(|x| x.parse::<usize>().unwrap())
                .collect();
            let c = cap[0];
            let repeat = cap[1];

            if recurse & data[idx + 1..idx + c + 1].contains(&'(') {
                let tmp = &data[idx + 1..idx + c + 1].iter().collect::<String>();
                length += repeat * decompress(tmp, recurse)
            } else {
                length += repeat * c;
            }

            idx += c + 1;
            FLAG = false;
            capture.clear();
            continue;
        } else if FLAG {
            capture.push(*data.get(idx as usize).unwrap());
        } else if *data.get(idx as usize).unwrap() == '(' {
            FLAG = true;
        } else {
            length += 1;
        }
        idx += 1;
    }
    length
}

fn main() {
    let data = include_str!("../day09.txt").trim();
    let p1 = decompress(data, false);
    println!("Part 1: {}", p1);

    let p2 = decompress(data, true);
    println!("Part 2: {}", p2);
}
