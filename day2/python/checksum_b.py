#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    file = open(sys.argv[1]).read().splitlines()
    converted = [[int(digit) for digit in line.split()] for line in file]

    checksum = 0
    for item in converted:
        for i in range(0, len(item)):
            for j in range(0, len(item)):
                if item[i] % item[j] == 0 and i != j:
                    checksum += int(item[i] / item[j])

    print(checksum)
