#!/usr/bin/python3

import sys

def checkIfAnagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def checkLineForAnagrams(line):
    for i in range(0, len(line)):
        for j in range(0, len(line)):
            if i != j and checkIfAnagrams(line[i], line[j]):
                return True
    return False

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    file = open(sys.argv[1]).read().splitlines()
    valid = 0
    for line in (entry.split() for entry in file):
        if not checkLineForAnagrams(line):
            valid += 1

print(valid)
