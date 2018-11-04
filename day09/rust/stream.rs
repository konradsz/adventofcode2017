use std::fs;

fn remove_garbage(mut stream: String) -> String {
    let has_garbage = |s: &str| {
        if let Some(_) = s.find("<") {
            return true;
        }
        false
    };

    stream = stream.replace("!!", "");

    let mut garbage_length = 0;
    while has_garbage(&stream) {
        let begin = stream.find("<").unwrap();
        let mut end = stream.find(">").unwrap();
        while stream.chars().nth(end - 1).unwrap() == '!' {
            end += (&stream[end + 1..]).find(">").unwrap() + 1;
        }
        let marks = stream[begin..=end].matches('!').count();
        stream.replace_range(begin..=end, "");
        garbage_length += end - begin - 1 - 2 * marks;
    }
    println!("{}", garbage_length);
    stream
}

fn calculate_score(stream: &str) -> u32 {
    let mut total_score = 0;
    let mut current_value = 0;

    for c in stream.chars() {
        if c == '{' {
            current_value += 1;
            total_score += current_value;
        } else if c == '}' {
            current_value -= 1;
        }
    }
    total_score
}

fn main() {
    let stream = fs::read_to_string("../input").expect("file not found");
    println!("{}", calculate_score(&remove_garbage(stream)));
}
