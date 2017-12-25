#!/usr/bin/python3

tape = [0]
position = 0
state = 0

def step(*arg):
    global tape
    global position
    global state

    if tape[position] == 0:
        tape[position] = arg[0][0]
        position += arg[1][0]
        state = arg[2][0]
    elif tape[position] == 1:
        tape[position] = arg[0][1]
        position += arg[1][1]
        state = arg[2][1]

    if position < 0:
        tape = [0] + tape
        position += 1
    elif position == len(tape):
        tape = tape + [0]

for i in range(12134527):
    if   state == 0: step((1, 0), (1, -1),  (1, 2)) # state A
    elif state == 1: step((1, 1), (-1, 1),  (0, 2)) # state B
    elif state == 2: step((1, 0), (1, -1),  (0, 3)) # state C
    elif state == 3: step((1, 1), (-1, -1), (4, 2)) # state D
    elif state == 4: step((1, 1), (1, 1),   (5, 0)) # state E
    elif state == 5: step((1, 1), (1, 1),   (0, 4)) # state F

print(tape.count(1))
