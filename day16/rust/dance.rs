use std::fs;

fn spin(programs: &mut [char], size: usize) {
    let mut reversed: [char; 16] = ['a'; 16];
    {
        let front = &programs[0..programs.len() - size];
        let back = &programs[programs.len() - size..];
        for (i, letter) in back.iter().chain(front.iter()).enumerate() {
            reversed[i] = *letter;
        }
    }

    for (to, from) in programs.iter_mut().zip(reversed.iter()) {
        *to = *from;
    }
}

fn exchange(programs: &mut [char], position_1: usize, position_2: usize) {
    let (program_1, program_2) = (programs[position_1], programs[position_2]);
    programs[position_1] = program_2;
    programs[position_2] = program_1;
}

fn partner(programs: &mut [char], program_1: char, program_2: char) {
    let position_1 = programs.iter().position(|program| *program == program_1).unwrap();
    let position_2 = programs.iter().position(|program| *program == program_2).unwrap();
    programs[position_1] = program_2;
    programs[position_2] = program_1;
}

fn main() {
    let mut programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'];
    let mut programs_combinations: Vec<[char; 16]> = Vec::new();
    programs_combinations.push(programs);

    let content = fs::read_to_string("../input").expect("file not found");

    for i in 0..1_000_000_000 {
        for step in content.trim().split(',') {
            match &step[0..1] {
                "s" => {
                    let size = step[1..].parse().unwrap();
                    spin(&mut programs, size);
                },
                "x" => {
                    let positions: Vec<usize> = step[1..].split('/').map(|number| number.parse().unwrap()).collect();
                    exchange(&mut programs, positions[0], positions[1]);
                },
                "p" => {
                    let program_1 = step[1..2].chars().next().unwrap();
                    let program_2 = step[3..4].chars().next().unwrap();
                    partner(&mut programs, program_1, program_2);
                },
                _ => println!("unknown step")
            }
        }
        if programs_combinations.contains(&programs) {
            programs = programs_combinations[1_000_000_000 % (i + 1)];
            break;
        }
        else {
            programs_combinations.push(programs);
        }
    }

    println!("After 1 iteration: {}", programs_combinations[1].iter().collect::<String>());
    println!("After 1_000_000_000 iterations: {}", programs.iter().collect::<String>());
}
