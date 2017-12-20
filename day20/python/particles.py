#!/usr/bin/python3

import sys
from math import sqrt
from operator import add

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.destroyed = False

    def update(self):
        self.velocity = list(map(add, self.velocity, self.acceleration))
        self.position = list(map(add, self.position, self.velocity))

    def calculateAccelerationMagnitude(self):
        return sqrt(sum([a ** 2 for a in self.acceleration]))

    def markDestroyedIfCollides(self, particle):
        if self.position == particle.position:
            self.destroyed = particle.destroyed = True

if len(sys.argv) != 2:
    print('Provide input file as command line argument!')
else:
    particles = []
    for particle in open(sys.argv[1]).read().splitlines():
        p_begin = particle.index('<')
        p_end = particle.index('>', p_begin)
        v_begin = particle.index('<', p_end)
        v_end = particle.index('>', v_begin)
        a_begin = particle.index('<', v_end)
        a_end = particle.index('>', a_begin)
        p = [int(i) for i in particle[p_begin + 1:p_end].split(',')]
        v = [int(i) for i in particle[v_begin + 1:v_end].split(',')]
        a = [int(i) for i in particle[a_begin + 1:a_end].split(',')]
        particles.append(Particle(p, v, a))

    numberOfParticles = len(particles)

    # PART 1: works only when there is only one particle with lowest value of acceleration magnitude
    magnitudes = [particle.calculateAccelerationMagnitude() for particle in particles]
    print('Index of particle closest to (0,0,0) in the long term:', magnitudes.index(min(magnitudes)))

    # PART 2: dirty solution, simulate as long as number of particles isn't changing anymore
    for _ in range(10000):
        for i in range(numberOfParticles):
            for j in range(i + 1, numberOfParticles):
                particles[i].markDestroyedIfCollides(particles[j])
        particles = [particle for particle in particles if not particle.destroyed]

        for i, particle in enumerate(particles):
            particle.update()

        numberOfParticles = len(particles)
        print(numberOfParticles)

