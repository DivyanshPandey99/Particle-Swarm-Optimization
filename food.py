import pygame

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
