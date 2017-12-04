#!/usr/bin/python3

import sys

#if len(sys.argv) != 2:
#    print("Provide input file as command line argument!")
#else:
#    file = open(sys.argv[1]).read().splitlines()
#    valid = 0
#    for entry in file:
#        extended = entry.split()#.append([item[::-1] for item in entry.split()])
#        extended += [item[::-1] for item in entry.split()]
#        if len(entry.split()) * 2 == len(set(extended)):
#            valid += 1

    #print(valid)

def checkIfAnagrams(word1, word2):
    return len(word1) == len(word2) and len(set(word1) | set(word2)) == len(word1)

print(checkIfAnagrams("asd", "dsa1"))


