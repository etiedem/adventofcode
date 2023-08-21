use itertools::{iproduct, Itertools};

fn parse_store_section(data: &str) -> Vec<(u32, u32, u32)> {
    data.lines()
        .skip(1)
        .map(|line| {
            let mut parts = line.split_whitespace();
            let armor = parts.nth_back(0).unwrap().parse().unwrap();
            let damage = parts.nth_back(0).unwrap().parse().unwrap();
            let cost = parts.nth_back(0).unwrap().parse().unwrap();
            (cost, damage, armor)
        })
        .collect()
}
fn parse_store(
    data: &str,
) -> (
    Vec<(u32, u32, u32)>,
    Vec<(u32, u32, u32)>,
    Vec<(u32, u32, u32)>,
) {
    let mut parts = data.split("\n\n");
    let weapons = parse_store_section(parts.next().unwrap());
    let armor = parse_store_section(parts.next().unwrap());
    let rings = parse_store_section(parts.next().unwrap());
    (weapons, armor, rings)
}

fn parse_boss(data: &str) -> (u32, u32, u32) {
    data.lines()
        .map(|line| line.split_whitespace().last().unwrap().parse().unwrap())
        .collect_tuple()
        .unwrap()
}

fn player_wins(player: (u32, u32, u32), boss: (u32, u32, u32)) -> bool {
    let player_damage = player.1.saturating_sub(boss.2);
    let boss_damage = boss.1.saturating_sub(player.2);
    if boss_damage == 0 {
        return true;
    }
    let player_turns = boss.0 / player_damage;
    let boss_turns = player.0 / boss_damage;
    player_turns <= boss_turns
}

fn solve(
    boss: (u32, u32, u32),
    weapons: Vec<(u32, u32, u32)>,
    armor: Vec<(u32, u32, u32)>,
    rings: Vec<(u32, u32, u32)>,
) -> (u32, u32) {
    let mut min_cost = u32::MAX;
    let mut max_cost = u32::MIN;

    for (w, a, r1, r2) in iproduct!(&weapons, &armor, &rings, &rings) {
        if r1 == r2 {
            continue;
        }
        let player = (100, w.1 + r1.1 + r2.1, a.2 + r1.2 + r2.2);
        let c_cost = w.0 + a.0 + r1.0 + r2.0;
        if c_cost == 9 {
            println!("{:?}, {:?}, {:?}, {:?}", w, a, r1, r2);
        }
        if c_cost < min_cost && player_wins(player, boss) {
            min_cost = c_cost;
        }
        if c_cost > max_cost && !player_wins(player, boss) {
            max_cost = c_cost;
        }
    }
    (min_cost, max_cost)
}
fn main() {
    let boss = parse_boss(include_str!("input.txt"));
    let (weapons, mut armor, mut rings) = parse_store(include_str!("store.txt"));
    armor.push((0, 0, 0)); // No armor
    rings.push((0, 0, 0)); // No rings

    let (p1, p2) = solve(boss, weapons, armor, rings);

    println!("Part 1: {}", p1);
    println!("Part 2: {}", p2);
}
