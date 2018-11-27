use std::fs;

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn extend(grid: &mut Vec<Vec<char>>) {
    let size = grid.len();
    for row in grid.iter_mut() {
        row.insert(0, '.');
        row.push('.');
    }
    grid.insert(0, vec!['.'; size + 2]);
    grid.push(vec!['.'; size + 2]);
}

fn turn_right(direction: &mut Direction) {
    match *direction {
        Direction::Up => *direction = Direction::Right,
        Direction::Down => *direction = Direction::Left,
        Direction::Left => *direction = Direction::Up,
        Direction::Right => *direction = Direction::Down,
    }
}

fn turn_left(direction: &mut Direction) {
    match *direction {
        Direction::Up => *direction = Direction::Left,
        Direction::Down => *direction = Direction::Right,
        Direction::Left => *direction = Direction::Down,
        Direction::Right => *direction = Direction::Up,
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");
    let mut grid: Vec<Vec<char>> = Vec::new();

    for line in content.lines() {
        let chars: Vec<char> = line.chars().collect();
        grid.push(chars);
    }

    let mut direction = Direction::Up;
    let middle = (grid.len() as f64 / 2.0).ceil() as usize;
    let mut position = (middle - 1, middle - 1);
    let mut counter = 0;

    for _ in 0..10_000 {
        if grid[position.1][position.0] == '#' {
            grid[position.1][position.0] = '.';
            turn_right(&mut direction);
        } else if grid[position.1][position.0] == '.' {
            grid[position.1][position.0] = '#';
            turn_left(&mut direction);
            counter += 1
        }

        let mut iposition: (isize, isize) = (position.0 as isize, position.1 as isize);
        match direction {
            Direction::Up => iposition = (iposition.0, iposition.1 - 1),
            Direction::Down => iposition = (iposition.0, iposition.1 + 1),
            Direction::Left => iposition = (iposition.0 - 1, iposition.1),
            Direction::Right => iposition = (iposition.0 + 1, iposition.1),
        }
        if iposition.0 as usize == grid.len()
            || iposition.1 as usize == grid.len()
            || iposition.0 < 0
            || iposition.1 < 0
        {
            extend(&mut grid);
            position = ((iposition.0 + 1) as usize, (iposition.1 + 1) as usize);
        } else {
            position = (iposition.0 as usize, iposition.1 as usize);
        }
    }

    println!("{}", counter);
}
