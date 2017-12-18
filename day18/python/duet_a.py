#!/usr/bin/python3

import sys

registers = {}
frequency = 0
pc = 0
recovered = False

def get(value):
    try:
        return int(value)
    except ValueError:
        return registers[value]

def execute(instruction):
    global pc
    global frequency
    global recovered

    if instruction[1] not in registers:
        registers[instruction[1]] = 0

    pc += 1

    if instruction[0] == 'snd':
        frequency = registers[instruction[1]]
    elif instruction[0] == 'set':
        registers[instruction[1]] = get(instruction[2])
    elif instruction[0] == 'add':
        registers[instruction[1]] += get(instruction[2])
    elif instruction[0] == 'mul':
        registers[instruction[1]] = registers[instruction[1]] * get(instruction[2])
    elif instruction[0] == 'mod':
        registers[instruction[1]] = registers[instruction[1]] % get(instruction[2])
    elif instruction[0] == 'rcv':
        if registers[instruction[1]] > 0:
            print(frequency)
            recovered = True
    elif instruction[0] == 'jgz':
        if registers[instruction[1]] > 0:
            pc += get(instruction[2]) - 1

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    instructions = open(sys.argv[1]).read().splitlines()
    while pc < len(instructions) and not recovered:
        execute(instructions[pc].split())

