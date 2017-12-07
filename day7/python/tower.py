#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    notTops = [line.strip() for line in open(sys.argv[1]).readlines() if '->' in line]
    parents = {entry.split()[0] for entry in notTops}
    children = {program.strip() for entry in notTops for program in entry[entry.find('->') + 3:].split(',')}
    print(parents - children)

