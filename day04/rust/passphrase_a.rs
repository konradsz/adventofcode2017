use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;

fn main() {
    let contents = fs::read_to_string("../input")
        .expect("file not found");

    let mut count = 0;

    for line in contents.lines() {
        let words: Vec<&str> = line.split_whitespace().collect();
        let words_len = words.len();
        let hash: HashSet<&str> = HashSet::from_iter(words);
        if words_len == hash.len() {
            count += 1;
        }
    }

    println!("{}", count);
}
