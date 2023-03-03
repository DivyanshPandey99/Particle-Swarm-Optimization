import random
import math

class PSO:
    def __init__(self, swarm, food):
        self.swarm = swarm
        self.food = food
        self.global_best_x = random.uniform(0, 1)
        self.global_best_y = random.uniform(0, 1)
        self.global_best_fitness = 0

    def update(self):
        for particle in self.swarm.particles:
            w = 0.5
            c1 = 1
            c2 = 10
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)

            # Code for PSO Algorithm function to update the particle velocity based on fitness
            particle.vx = w * particle.vx + c1 * r1 * (particle.best_x - particle.x) + c2 * r2 * (self.global_best_x - particle.x)
            particle.vy = w * particle.vy + c1 * r1 * (particle.best_y - particle.y) + c2 * r2 * (self.global_best_y - particle.y)
            particle.update()
            particle.evaluate(self.food)

            # Updating thr global best fitness if current fitness is better
            if particle.fitness > self.global_best_fitness:
                self.global_best_x = particle.x
                self.global_best_y = particle.y
                self.global_best_fitness = particle.fitness
