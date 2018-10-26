use std::fs;

fn main() {
    let contents = fs::read_to_string("../input")
        .expect("file not found");

    let mut maze: Vec<i32> = Vec::new();
    let mut current_position: i32 = 0;
    let mut steps = 0;

    for line in contents.lines() {
        maze.push(line.parse().unwrap());
    }

    loop {
        if current_position >= maze.len() as i32 {
            break;
        }

        let offset = maze[current_position as usize];
        maze[current_position as usize] += 1;
        current_position += offset;
        steps += 1;
    }

    println!("{}", steps);
}
