#!/usr/bin/python3

import sys

def removeGarbage(stream):
    hasGarbage = lambda s: s.find('<') > 0

    stream = stream.replace('!!', '')
    totalGarbageLength = 0

    while hasGarbage(stream):
        begin = stream.find('<')
        end = stream.find('>')
        while stream[end - 1] == '!' and stream[end - 2] != '!':
            end = stream.find('>', end + 1)

        garbage = stream[begin + 1:end]
        marks = garbage.count('!')
        totalGarbageLength += len(garbage) - marks * 2
        stream = stream[0:begin] + stream[end + 1:]

    stream = stream.replace(',', '')
    print('Removed garbage length:', totalGarbageLength)
    return stream

def calculateScore(stream):
    score = 0
    current = 1
    for i in range(0, len(stream)):
        if stream[i] == '{':
            score += current
            current += 1
        elif stream[i] == '}':
            current -= 1
    return score

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    stream = open(sys.argv[1]).read()
    stream = removeGarbage(stream)
    print('Score:', calculateScore(stream))
