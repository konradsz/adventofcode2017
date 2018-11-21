fn spinlock_a() {
    let mut buffer = vec![0];

    let mut current_position = 0;
    let steps = 367;

    for i in 1..=2017 {
        current_position += steps;
        while current_position >= buffer.len() {
            current_position -= buffer.len();
        }
        current_position += 1;
        buffer.insert(current_position, i);
    }

    let index = buffer.iter().position(|&number| number == 2017).unwrap();
    println!("{}", buffer[index + 1]);
}

fn spinlock_b() {
    let mut buffer_length = 1;

    let mut current_position = 0;
    let steps = 367;
    let mut value = 0;

    for i in 1..=50_000_000 {
        current_position += steps;
        while current_position >= buffer_length {
            current_position -= buffer_length;
        }

        if current_position == 0 {
            value = i;
        }

        current_position += 1;
        buffer_length += 1;
    }

    println!("{}", value);
}

fn main() {
    spinlock_a();
    spinlock_b();
}
