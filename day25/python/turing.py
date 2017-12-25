#!/usr/bin/python3

tape = [0]
position = 0
state = 0

def step(value, move, newState):
    global tape
    global position
    global state

    tape[position] = value
    position += move
    if position < 0:
        tape = [0] + tape
        position += 1
    elif position == len(tape):
        tape = tape + [0]
    state = newState

for _ in range(12134527):
    if state == 0: # state A
        if tape[position] == 0:
            step(1, 1, 1)
        elif tape[position] == 1:
            step(0, -1, 2)
    elif state == 1: # state B
        if tape[position] == 0:
            step(1, -1, 0)
        elif tape[position] == 1:
            step(1, 1, 2)
    elif state == 2: # state C
        if tape[position] == 0:
            step(1, 1, 0)
        elif tape[position] == 1:
            step(0, -1, 3)
    elif state == 3: # state D
        if tape[position] == 0:
            step(1, -1, 4)
        elif tape[position] == 1:
            step(1, -1, 2)
    elif state == 4: # state E
        if tape[position] == 0:
            step(1, 1, 5)
        elif tape[position] == 1:
            step(1, 1, 0)
    elif state == 5: # state F
        if tape[position] == 0:
            step(1, 1, 0)
        elif tape[position] == 1:
            step(1, 1, 4)

print(tape.count(1))
