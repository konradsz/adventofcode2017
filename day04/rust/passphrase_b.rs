use std::fs;

fn check_if_anagrams(word1: &str, word2: &str) -> bool {
    let mut word1_chars: Vec<char> = word1.chars().collect();
    let mut word2_chars: Vec<char> = word2.chars().collect();
    word1_chars.sort_unstable();
    word2_chars.sort_unstable();

    return word1_chars == word2_chars;
}

fn check_line_for_anagrams(line: &Vec<&str>) -> bool {
    for (i, word1) in line.iter().enumerate() {
        for (j, word2) in line.iter().enumerate() {
            if i != j && check_if_anagrams(word1, word2) {
                return true;
            }
        }
    }
    false
}

fn main() {
    let contents = fs::read_to_string("../input")
        .expect("file not found");

    let mut count = 0;

    for line in contents.lines() {
        let words: Vec<&str> = line.split_whitespace().collect();
        if !check_line_for_anagrams(&words) {
            count += 1;
        }
    }

    println!("{}", count);
}
