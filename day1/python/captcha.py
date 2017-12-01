#!/usr/bin/python3

import sys

def solveCaptcha(input1, input2):
    result = 0
    for first, second in zip(input1, input2):
        if first == second:
            result += first

    return result

if len(sys.argv) != 2:
    print("Provide input file as command line argument!")
else:
    integerListInput = [int(digit) for digit in open(sys.argv[1]).read() if digit.isdigit()]

    print(solveCaptcha(integerListInput, integerListInput[1:] + [integerListInput[0]]))

    middle = int(len(integerListInput) / 2)
    print(solveCaptcha(integerListInput, integerListInput[middle:] + integerListInput[:middle]))

