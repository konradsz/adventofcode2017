use std::collections::HashMap;
use std::fs;

fn caught(depth: u32, height: u32) -> bool {
    (depth % ((height - 1) * 2)) == 0
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut firewall = HashMap::new();

    for line in content.lines() {
        let mut layer = line.split(": ");
        let depth = layer.next().unwrap().parse::<u32>().unwrap();
        let height = layer.next().unwrap().parse::<u32>().unwrap();
        firewall.insert(depth, height);
    }

    let mut severity = 0;
    for layer in &firewall {
        if caught(*layer.0, *layer.1) {
            severity += *layer.0 * *layer.1;
        }
    }

    println!("Severity: {}", severity);

    let mut delay = 0;
    loop {
        if firewall
            .iter()
            .all(|layer| !caught(*layer.0 + delay, *layer.1))
        {
            break;
        }
        delay += 1;
    }

    println!("{}", delay);
}
