import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.maxspeed = 3
        self.best_x = x
        self.best_y = y
        self.fitness = 0
        self.best_fitness = 0

    def update(self):
        speed = (self.vx**2 + self.vy**2)**0.5
        if(speed>self.maxspeed):
            self.vx = self.vx*self.maxspeed/speed
            self.vy = self.vy*self.maxspeed/speed
        self.x += self.vx
        self.y += self.vy

    def evaluate(self, food):
        dx = self.x - food.x
        dy = self.y - food.y
        distance = (dx**2 + dy**2)**0.5
        self.fitness = 1 / distance

        if self.fitness > self.best_fitness:
            self.best_x = self.x
            self.best_y = self.y
            self.best_fitness = self.fitness
