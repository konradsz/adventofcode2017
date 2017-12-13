#!/usr/bin/python3

import sys
import itertools

def caught(depth, height):
    return (depth % ((height - 1) * 2)) == 0

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    file = open(sys.argv[1]).read().splitlines()

    firewall = {}
    for line in file:
        depth, height = map(int, line.split(': '))
        firewall[depth] = height

    severity = 0
    for layer in firewall:
        if caught(layer, firewall[layer]):
            severity += (layer * firewall[layer])

    print('Severity:', severity)

    for delay in itertools.count():
        stop = True
        for layer in firewall:
            if caught(layer + delay, firewall[layer]):
                stop = False
                break

        if stop:
            print('Delay:', delay)
            break

