#!/usr/bin/python3

input = 367
buffer = [0]
currentPosition = 0

for i in range(2017):
    currentPosition = (currentPosition + input)
    while currentPosition >= len(buffer):
        currentPosition -= len(buffer)

    buffer.insert(currentPosition + 1, i + 1)
    currentPosition += 1

print('Value after 2017 in buffer:', buffer[currentPosition + 1])
