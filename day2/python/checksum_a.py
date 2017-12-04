#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    file = open(sys.argv[1]).read().splitlines()
    converted = [[int(digit) for digit in line.split()] for line in file]

    checksum = 0
    for item in converted:
        checksum += max(item) - min(item)

    print(checksum)
