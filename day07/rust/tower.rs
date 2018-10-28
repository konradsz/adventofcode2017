use std::collections::HashSet;
use std::fs;

struct Entry {
    name: String,
    weight: u32,
    children: Vec<String>,
}

impl Entry {
    fn new(name: String, weight: u32, children: Vec<String>) -> Entry {
        Entry {
            name,
            weight,
            children,
        }
    }
}

fn find_root(entries: &Vec<Entry>) -> &str {
    let is_child = |name| entries.iter().any(|entry| entry.children.contains(name));

    for entry in entries {
        if !entry.children.is_empty() && !is_child(&entry.name) {
            return &entry.name;
        }
    }
    ""
}

fn get_subtree_weight(entries: &Vec<Entry>, name: &str) -> u32 {
    for entry in entries {
        if entry.name == name {
            let mut weight = entry.weight;
            for child in &entry.children {
                weight += get_subtree_weight(entries, &child);
            }
            return weight;
        }
    }
    0
}

fn find_imbalance(entries: &Vec<Entry>, root: &str) {
    let get_weight = |name: &str| {
        for entry in entries {
            if entry.name == name {
                return entry.weight;
            }
        }
        0
    };

    for entry in entries {
        if entry.name == root {
            let mut max_weight = 0;
            let mut max_name = "";
            let mut weights = HashSet::new();

            for child in &entry.children {
                let weight = get_subtree_weight(entries, child);
                weights.insert(weight);
                if weight > max_weight {
                    max_weight = weight;
                    max_name = child;
                }
            }
            if weights.len() > 1 {
                let max = weights.iter().max().unwrap();
                let min = weights.iter().min().unwrap();
                println!(
                    "Imbalance found! node name: {}, weight: {}, difference: {}",
                    max_name,
                    get_weight(max_name),
                    max - min
                );
                find_imbalance(entries, max_name);
            }
        }
    }
}

fn main() {
    let content = fs::read_to_string("../input").expect("file not found");

    let mut entries = Vec::new();

    for line in content.lines() {
        let mut parts_iter = line.split_whitespace();
        let name = parts_iter.next().unwrap().to_string();
        let brackets: &[_] = &['(', ')'];
        let weight = parts_iter
            .next()
            .unwrap()
            .trim_matches(brackets)
            .parse::<u32>()
            .unwrap();
        let children = match parts_iter.next() {
            Some(_) => {
                let mut parts = Vec::new();
                for part in parts_iter {
                    parts.push(part.trim_matches(',').to_string());
                }
                parts
            }
            None => Vec::new(),
        };

        entries.push(Entry::new(name, weight, children));
    }

    let root = find_root(&entries);
    println!("Root: {}", root);

    find_imbalance(&entries, root);
}
