from particle import Particle
import random
from paramaters import *

class Swarm:
    def __init__(self, size):
        self.particles = self.initializeparticle(size)

    def initializeparticle(self,size):
        particles = []
        for i in range(size):
            particles.append(Particle(random.randint(10,SCREEN_WIDTH-10), random.randint(10,SCREEN_HEIGHT-10)))
        return particles

    def update(self, food):
        for particle in self.particles:
            particle.evaluate(food)
            particle.update()
