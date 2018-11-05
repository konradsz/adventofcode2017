fn main() {
    const SIZE: usize = 256;
    let mut list = Vec::new();

    for i in 0..SIZE {
        list.push(i as usize);
    }

    let input = [
        31, 2, 85, 1, 80, 109, 35, 63, 98, 255, 0, 13, 105, 254, 128, 33,
    ];
    let mut current_position: usize = 0;
    let mut skip_size: usize = 0;

    for length in input.iter() {
        let sublist_end = current_position + length;
        if sublist_end < SIZE {
            let mut preceding_sublist = list[..current_position].to_vec();
            let mut sublist = list[current_position..sublist_end].to_vec();
            let mut succeeding_sublist = list[sublist_end..].to_vec();
            sublist.reverse();

            list.clear();
            list.append(&mut preceding_sublist);
            list.append(&mut sublist);
            list.append(&mut succeeding_sublist)
        } else {
            let head = current_position;
            let head_length = SIZE - head;
            let tail = sublist_end - SIZE;

            let mut head_half = list[head..].to_vec();
            let mut tail_half = list[..tail].to_vec();
            let mut middle = list[tail..head].to_vec();
            let mut sublist = Vec::new();
            sublist.append(&mut head_half);
            sublist.append(&mut tail_half);
            sublist.reverse();

            list.clear();
            list.append(&mut sublist[head_length..].to_vec());
            list.append(&mut middle);
            list.append(&mut sublist[..head_length].to_vec());
        }

        current_position = (current_position + length + skip_size) % SIZE;
        skip_size += 1;
    }

    println!("result: {}", list[0] * list[1]);
}
