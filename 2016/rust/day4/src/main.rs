use counter::Counter;

struct Room {
    room: String,
    sector: u32,
    checksum: String,
}

impl From<&str> for Room {
    fn from(value: &str) -> Self {
        let (room, rest) = value.rsplit_once('-').unwrap();
        let (sector, rest) = rest.split_once('[').unwrap();
        let sector: u32 = sector.parse().unwrap();
        let checksum = rest.trim_end_matches(']');
        Room {
            room: room.to_string(),
            sector,
            checksum: checksum.to_string(),
        }
    }
}

impl Room {
    fn valid(&self) -> bool {
        let counter = self
            .room
            .chars()
            .filter(|x| x != &'-')
            .collect::<Counter<_>>();

        if counter
            .most_common_tiebreaker(|&a, &b| a.cmp(&b))
            .iter()
            .take(5)
            .map(|(char, _)| char)
            .collect::<String>()
            == self.checksum
        {
            return true;
        }
        false
    }

    fn decrypt(&self) -> String {
        let tmp = self.room.as_bytes();
        let mut output = String::new();
        for x in tmp {
            if x == &b'-' {
                output.push(' ');
                continue;
            }
            output.push_str(&String::from_utf8_lossy(&[((((x - 97)
                + (self.sector % 26) as u8)
                % 26)
                + 97_u8)]));
        }
        output
    }
}

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(Room::from)
        .filter(|room| room.valid())
        .map(|room| room.sector)
        .sum()
}

fn part2(input: &str) -> u32 {
    input
        .lines()
        .map(Room::from)
        .filter(|room| room.valid())
        .filter(|room| room.decrypt().contains("north"))
        .map(|room| room.sector)
        .next()
        .unwrap()
}
fn main() {
    let data = include_str!("input.txt");
    println!("Part 1: {}", part1(data));
    println!("Part 2: {}", part2(data));
}
