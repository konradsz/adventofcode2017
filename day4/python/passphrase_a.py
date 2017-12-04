#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    file = open(sys.argv[1]).read().splitlines()
    print(sum(1 if len(entry.split()) == len(set(entry.split())) else 0 for entry in file))
