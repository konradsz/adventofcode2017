#!/usr/bin/python3

import sys

registers = {}
frequency = 0
pc = 0
recovered = False

def execute(instruction):
    global pc
    global frequency
    global recovered

    if instruction[1] not in registers:
        registers[instruction[1]] = 0

    if instruction[0] == 'snd':
        frequency = registers[instruction[1]]
        pc += 1
    elif instruction[0] == 'set':
        if instruction[2].isalpha():
            registers[instruction[1]] = registers[instruction[2]]
        else:
            registers[instruction[1]] = int(instruction[2])
        pc += 1
    elif instruction[0] == 'add':
        if instruction[2].isalpha():
            registers[instruction[1]] += registers[instruction[2]]
        else:
            registers[instruction[1]] += int(instruction[2])
        pc += 1
    elif instruction[0] == 'mul':
        registers[instruction[1]] = registers[instruction[1]] * int(instruction[2])
        pc += 1
    elif instruction[0] == 'mod':
        if instruction[2].isalpha():
            registers[instruction[1]] = registers[instruction[1]] % registers[instruction[2]]
        else:
            registers[instruction[1]] = registers[instruction[1]] % int(instruction[2])
        pc += 1
    elif instruction[0] == 'rcv':
        if registers[instruction[1]] > 0:
            print(frequency)
            recovered = True
        pc += 1
    elif instruction[0] == 'jgz':
        if registers[instruction[1]] > 0:
            if instruction[2].isalpha():
                pc += registers[instruction[2]]
            else:
                pc += int(instruction[2])
        else:
            pc += 1

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    instructions = open(sys.argv[1]).read().splitlines()
    while pc < len(instructions) and not recovered:
        execute(instructions[pc].split())

