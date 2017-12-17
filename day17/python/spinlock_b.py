#!/usr/bin/python3

input = 367
bufferLength = 1
currentPosition = 0
value = 0

for i in range(50000000):
    currentPosition = (currentPosition + input)
    while currentPosition >= bufferLength:
        currentPosition -= bufferLength

    if currentPosition == 0:
        value = i + 1

    currentPosition += 1
    bufferLength += 1

print('Value after 0 in 50000000th iteration:', value)
