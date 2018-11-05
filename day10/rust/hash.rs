struct Hash {
    size: usize,
    list: Vec<usize>,
    current_position: usize,
    skip_size: usize
}

impl Hash {
    fn new(size: usize) -> Hash {
        let mut list = Vec::new();
        for i in 0..size {
            list.push(i as usize);
        }

        Hash {
            size,
            list,
            current_position: 0,
            skip_size: 0
        }
    }

    fn reorder_list(&mut self, input: &Vec<usize>) {
        for length in input.iter() {
            let sublist_end = self.current_position + length;
            if sublist_end < self.size {
                let mut preceding_sublist = self.list[..self.current_position].to_vec();
                let mut sublist = self.list[self.current_position..sublist_end].to_vec();
                let mut succeeding_sublist = self.list[sublist_end..].to_vec();
                sublist.reverse();

                self.list.clear();
                self.list.extend(&preceding_sublist);
                self.list.extend(&sublist);
                self.list.extend(&succeeding_sublist)
            } else {
                let head = self.current_position;
                let head_length = self.size - head;
                let tail = sublist_end - self.size;

                let mut head_half = self.list[head..].to_vec();
                let mut tail_half = self.list[..tail].to_vec();
                let mut middle = self.list[tail..head].to_vec();
                let mut sublist = Vec::new();
                sublist.extend(&head_half);
                sublist.extend(&tail_half);
                sublist.reverse();

                self.list.clear();
                self.list.extend(&sublist[head_length..]);
                self.list.extend(&middle);
                self.list.extend(&sublist[..head_length]);
            }

            self.current_position = (self.current_position + length + self.skip_size) % self.size;
            self.skip_size += 1;
        }
    }

    fn calculate_hash(mut self, input: String) {
        let mut lengths: Vec<usize> = input.chars().map(|c| c as usize).collect();
        lengths.extend(&[17, 31, 73, 47, 23]);

        for _ in 0..64 {
            self.reorder_list(&lengths);
        }

        let mut hash = String::new();
        for i in 0..16 {
            let mut x: u8 = self.list[i * 16] as u8;
            for j in (i * 16 + 1)..(i * 16 + 16) {
                x ^= self.list[j] as u8;
            }
            hash.push_str(&format!("{:x}", x));
        }

        println!("Hash: {}", hash);
    }
}

fn main() {
    let mut hash = Hash::new(256);
    hash.reorder_list(&[31, 2, 85, 1, 80, 109, 35, 63, 98, 255, 0, 13, 105, 254, 128, 33].to_vec());
    println!("Result: {}", hash.list[0] * hash.list[1]);

    Hash::new(256).calculate_hash(String::from("31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"));
}
