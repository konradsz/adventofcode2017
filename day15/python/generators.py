#!/usr/bin/python3

import itertools

def generator1(startingValue, factor):
    previousValue = startingValue
    divisor = 2147483647

    for _ in itertools.count():
        previousValue = (previousValue * factor) % divisor
        yield previousValue

def generator2(startingValue, factor, multiples):
    previousValue = startingValue
    divisor = 2147483647

    for _ in itertools.count():
        previousValue = (previousValue * factor) % divisor
        if previousValue % multiples:
            continue
        else:
            yield previousValue

g_a1 = generator1(591, 16807)
g_b1 = generator1(393, 48271)

count = 0
for _ in range(0, 40000000):
    a, b = next(g_a1), next(g_b1)
    count += (a & 0xFFFF == b & 0xFFFF)
print('Part 1:', count)

g_a2 = generator2(591, 16807, 4)
g_b2 = generator2(393, 48271, 8)

count = 0
for _ in range(0, 5000000):
    a, b = next(g_a2), next(g_b2)
    count += (a & 0xFFFF == b & 0xFFFF)
print('Part 2:', count)

