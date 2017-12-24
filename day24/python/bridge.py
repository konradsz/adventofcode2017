#!/usr/bin/python3

import sys

strengths = []

def calcStrength(component):
    return component[0] + component[1]

def buildBridge(parts, port, strength):
    strengths.append(strength)
    connectors = [c for c in parts if c[0] == port or c[1] == port]
    for c in connectors:
        tmp = list(parts)
        tmp.pop(tmp.index(c))
        if c[0] == port:
            buildBridge(tmp, c[1], strength + calcStrength(c))
        else:
            buildBridge(tmp, c[0], strength + calcStrength(c))

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    components = open(sys.argv[1]).read().splitlines()
    components = [(int(c.split('/')[0]), int(c.split('/')[1])) for c in components]

    buildBridge(components, 0, 0)
    print(max(strengths))
