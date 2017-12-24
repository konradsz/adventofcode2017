#!/usr/bin/python3

import sys

bridges = []

def calcStrength(component):
    return component[0] + component[1]

def buildBridge(parts, port, strength, length):
    bridges.append((strength, length))
    connectors = [c for c in parts if c[0] == port or c[1] == port]
    for c in connectors:
        tmp = list(parts)
        tmp.pop(tmp.index(c))
        if c[0] == port:
            buildBridge(tmp, c[1], strength + calcStrength(c), length + 1)
        else:
            buildBridge(tmp, c[0], strength + calcStrength(c), length + 1)

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    components = open(sys.argv[1]).read().splitlines()
    components = [(int(c.split('/')[0]), int(c.split('/')[1])) for c in components]

    buildBridge(components, 0, 0, 0)
    print('Strongest:', max(bridges, key = lambda sl: sl[0])) # print the strongest

    longest = []
    bridge = bridges.pop(bridges.index(max(bridges, key = lambda sl: sl[1])))
    longest.append(bridge)
    while max(bridges, key = lambda sl: sl[1])[1] == bridge[1]:
        bridge = max(bridges, key = lambda sl: sl[1])
        longest.append(bridges.pop(bridges.index(bridge)))

    print('Strongest of the longest:', max(longest, key = lambda sl: sl[0])) # print the longest
