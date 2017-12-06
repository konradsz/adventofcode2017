#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    memory = [int(number) for number in open(sys.argv[1]).read().split()]
    size = len(memory)

    states = []
    states.append(list(memory))

    def cycle():
        cycle.counter += 1
        maxValue = max(memory)
        maxValueIndex = memory.index(maxValue)
        memory[maxValueIndex] = 0

        for i in range(maxValueIndex + 1, maxValueIndex + maxValue + 1):
            memory[i % size] += 1

    cycle.counter = 0
    while True:
        cycle()
        if memory in states: break
        else:
            states.append(list(memory))

    print(cycle.counter)
    previousOccurrence = states.index(memory)
    print(cycle.counter - previousOccurrence)

