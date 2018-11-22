use std::fs;

#[derive(Eq, PartialEq)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");
    let diagram: Vec<&str> = content.lines().collect();
    let mut position = (diagram[0].find('|').unwrap(), 0);
    let mut direction = Direction::Down;
    let mut letters = Vec::new();
    let mut steps = 0;

    while !diagram[position.1]
        .chars()
        .nth(position.0)
        .unwrap()
        .is_whitespace()
    {
        let character = diagram[position.1].chars().nth(position.0).unwrap();
        if character.is_alphabetic() {
            letters.push(character);
        } else if character == '+' {
            if direction == Direction::Right || direction == Direction::Left {
                if !diagram[position.1 + 1]
                    .chars()
                    .nth(position.0)
                    .unwrap()
                    .is_whitespace()
                {
                    direction = Direction::Down;
                } else if !diagram[position.1 - 1]
                    .chars()
                    .nth(position.0)
                    .unwrap()
                    .is_whitespace()
                {
                    direction = Direction::Up;
                }
            } else if direction == Direction::Up || direction == Direction::Down {
                if !diagram[position.1]
                    .chars()
                    .nth(position.0 + 1)
                    .unwrap()
                    .is_whitespace()
                {
                    direction = Direction::Right;
                } else if !diagram[position.1]
                    .chars()
                    .nth(position.0 - 1)
                    .unwrap()
                    .is_whitespace()
                {
                    direction = Direction::Left;
                }
            }
        }

        position = match direction {
            Direction::Up => (position.0, position.1 - 1),
            Direction::Down => (position.0, position.1 + 1),
            Direction::Left => (position.0 - 1, position.1),
            Direction::Right => (position.0 + 1, position.1),
        };
        steps += 1;
    }

    println!("{}", letters.iter().collect::<String>());
    println!("{}", steps);
}
