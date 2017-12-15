#!/usr/bin/python3

def generator1(startingValue, factor):
    previousValue = startingValue
    divisor = 2147483647

    while True:
        previousValue = (previousValue * factor) % divisor
        yield previousValue

def generator2(startingValue, factor, multiplesOf):
    previousValue = startingValue
    divisor = 2147483647

    while True:
        previousValue = (previousValue * factor) % divisor
        if not previousValue % multiplesOf:
            yield previousValue

g_a1 = generator1(591, 16807)
g_b1 = generator1(393, 48271)
count = sum((next(g_a1) & 0xFFFF == next(g_b1) & 0xFFFF) for _ in range(40000000))
print('Part 1:', count)

g_a2 = generator2(591, 16807, 4)
g_b2 = generator2(393, 48271, 8)
count = sum((next(g_a2) & 0xFFFF == next(g_b2) & 0xFFFF) for _ in range(5000000))
print('Part 2:', count)

