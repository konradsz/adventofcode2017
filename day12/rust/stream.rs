use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

fn find_connections(index: u32, connections: &HashMap<u32, Vec<u32>>, group: &mut HashSet<u32>) {
    group.insert(index);
    for connection in &connections[&index] {
        if !group.contains(connection) {
            find_connections(*connection, connections, group);
        }
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut connections = HashMap::new();

    for (i, line) in content.lines().enumerate() {
        let a: Vec<&str> = line.split_whitespace().collect();
        let connected_nodes: Vec<u32> = a[2..]
            .iter()
            .map(|c| c.trim_matches(',').parse::<u32>().unwrap())
            .collect();
        connections.insert(i as u32, connected_nodes);
    }

    {
        let mut group = HashSet::new();
        find_connections(0, &connections, &mut group);
        println!("Size of group with program 0: {}", group.len());
    }

    let mut connected_programs = HashSet::new();
    let mut current_index = 0;
    let mut number_of_groups = 0;

    while connected_programs.len() != connections.len() {
        if !connected_programs.contains(&current_index) {
            let mut group = HashSet::new();
            find_connections(current_index, &connections, &mut group);
            connected_programs.extend(group);
            number_of_groups += 1;
        }
        current_index += 1;
    }

    println!("Number of groups: {}", number_of_groups);
}
