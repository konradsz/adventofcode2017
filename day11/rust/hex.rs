use std::cmp::min;
use std::fs;

fn count_steps(steps: &Vec<&str>) -> u32 {
    let (mut n, mut ne, mut se, mut s, mut sw, mut nw) = (0, 0, 0, 0, 0, 0);
    for step in steps {
        match *step {
            "n" => n += 1,
            "ne" => ne += 1,
            "s" => s += 1,
            "se" => se += 1,
            "nw" => nw += 1,
            "sw" => sw += 1,
            _ => panic!("unknown direction!"),
        }
    }

    let mut steps: u32;

    // remove opposite steps
    steps = min(n, s);
    n -= steps;
    s -= steps;

    steps = min(ne, sw);
    ne -= steps;
    sw -= steps;

    steps = min(nw, se);
    nw -= steps;
    se -= steps;

    // combine steps
    steps = min(sw, se);
    sw -= steps;
    se -= steps;
    s += steps;

    steps = min(nw, ne);
    nw -= steps;
    ne -= steps;
    n += steps;

    steps = min(ne, s);
    ne -= steps;
    s -= steps;
    se += steps;

    steps = min(se, n);
    se -= steps;
    n -= steps;
    ne += steps;

    steps = min(nw, s);
    nw -= steps;
    s -= steps;
    sw += steps;

    steps = min(sw, n);
    sw -= steps;
    n -= steps;
    nw += steps;

    n + ne + se + s + sw + nw
}

fn main() {
    let mut hex = fs::read_to_string("../input").expect("file not found");
    hex = hex.trim().to_string();
    let steps = hex.split(',').collect();

    println!("{}", count_steps(&steps));

    let mut distances = Vec::new();
    for i in 0..steps.len() {
        distances.push(count_steps(&steps[0..i].to_vec()));
    }

    println!("{}", distances.iter().max().unwrap());
}
