#!/usr/bin/python3

import sys

registers = {}
highest = 0

def parse(instruction):
    instruction = instruction.split()
    reg = instruction[0]
    op = instruction[1]
    v = int(instruction[2])
    condReg = instruction[-3]
    cond = instruction[-2]
    condV = int(instruction[-1])

    def execute(register, operation, value):
        global highest

        if operation == 'inc':
            registers[register] = registers.get(register, 0) + value
        elif operation == 'dec':
            registers[register] = registers.get(register, 0) - value
        if registers[register] > highest:
            highest = registers[register]

    if (cond == '>' and registers.get(condReg, 0) > condV or
        cond == '<' and registers.get(condReg, 0) < condV or
        cond == '>=' and registers.get(condReg, 0) >= condV or
        cond == '<=' and registers.get(condReg, 0) <= condV or
        cond == '==' and registers.get(condReg, 0) == condV or
        cond == '!=' and registers.get(condReg, 0) != condV): execute(reg, op, v)


if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    for instruction in open(sys.argv[1]).read().splitlines():
        parse(instruction)

    print(max(list(registers.values())))
    print(highest)

