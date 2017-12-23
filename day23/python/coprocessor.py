#!/usr/bin/python3

import sys

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
pc = 0
counter = 0

def get(value):
    try:
        return int(value)
    except ValueError:
        return registers[value]

def execute(instruction):
    global pc
    global counter

    pc += 1

    if instruction[0] == 'set':
        registers[instruction[1]] = get(instruction[2])
    elif instruction[0] == 'sub':
        registers[instruction[1]] -= get(instruction[2])
    elif instruction[0] == 'mul':
        registers[instruction[1]] *= get(instruction[2])
        counter += 1
    elif instruction[0] == 'jnz':
        if get(instruction[1]) != 0:
            pc += get(instruction[2]) - 1

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    instructions = open(sys.argv[1]).read().splitlines()
    while pc < len(instructions):
        execute(instructions[pc].split())

    print(counter)
