#!/usr/bin/python3

import sys


class Program():
    def __init__(self, id, sndQ, rcvQ):
        self.sndQ = sndQ
        self.rcvQ = rcvQ
        self.waiting = False
        self.terminated = False
        self.pc = 0
        self.registers = {'p': id}
        self.sendCount = 0

    def execute(self, instruction):
        if instruction[1].isalpha() and instruction[1] not in self.registers:
            self.registers[instruction[1]] = 0

        if instruction[0] == 'snd':
            if instruction[1].isalpha():
                self.sndQ.append(self.registers[instruction[1]])
            else:
                self.sndQ.append(int(instruction[1]))
            self.sendCount += 1
            self.pc += 1
        elif instruction[0] == 'set':
            if instruction[2].isalpha():
                self.registers[instruction[1]] = self.registers[instruction[2]]
            else:
                self.registers[instruction[1]] = int(instruction[2])
            self.pc += 1
        elif instruction[0] == 'add':
            if instruction[2].isalpha():
                self.registers[instruction[1]] += self.registers[instruction[2]]
            else:
                self.registers[instruction[1]] += int(instruction[2])
            self.pc += 1
        elif instruction[0] == 'mul':
            self.registers[instruction[1]] = self.registers[instruction[1]] * int(instruction[2])
            self.pc += 1
        elif instruction[0] == 'mod':
            if instruction[2].isalpha():
                self.registers[instruction[1]] = self.registers[instruction[1]] % self.registers[instruction[2]]
            else:
                self.registers[instruction[1]] = self.registers[instruction[1]] % int(instruction[2])
            self.pc += 1
        elif instruction[0] == 'rcv':
            if len(self.rcvQ) > 0:
                self.waiting = False
                self.registers[instruction[1]] = self.rcvQ.pop(0)
                self.pc += 1
            else:
                self.waiting = True
        elif instruction[0] == 'jgz':
            if instruction[1].isalpha():
                condValue = self.registers[instruction[1]]
            else:
                condValue = int(instruction[1])
            if condValue > 0:
                if instruction[2].isalpha():
                    self.pc += self.registers[instruction[2]]
                else:
                    self.pc += int(instruction[2])
            else:
                self.pc += 1

    def run(self, instructions):
        if self.waiting and len(self.rcvQ) > 0:
            self.waiting = False

        while self.pc < len(instructions) and not self.waiting:
            self.execute(instructions[self.pc].split())

        if self.pc > len(instructions):
            self.terminated = True

    def isWaiting(self):
        return self.waiting

    def isTerminated(self):
        return self.terminated

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    instructions = open(sys.argv[1]).read().splitlines()
    queue0 = [] # queue of awaiting messages for program 0
    queue1 = [] # queue of awaiting messages for program 1

    program0 = Program(0, queue1, queue0)
    program1 = Program(1, queue0, queue1)

    while True:
        if not program0.isTerminated():
            program0.run(instructions)
        if not program1.isTerminated():
            program1.run(instructions)

        if (((program0.isWaiting() and program1.isWaiting()) and (len(queue0) == 0 and len(queue1) == 0)) or
            (program0.isTerminated() and program1.isTerminated())):
            print('Program 0 send counter:', program0.sendCount)
            print('Program 1 send counter:', program1.sendCount)
            break

