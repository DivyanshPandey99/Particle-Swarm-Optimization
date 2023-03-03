import pygame
from swarm import Swarm
from food import Food
from pso import PSO
from paramaters import *
from particle import Particle
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    swarm = Swarm(size=50)
    food = Food(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    pso = PSO(swarm, food)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                food = Food(pos[0],pos[1])
                for i in range(len(swarm.particles)):
                    swarm.particles[i] = Particle(swarm.particles[i].x,swarm.particles[i].y)
                pso = PSO(swarm, food)
                

        screen.fill((255, 255, 255))
        food.draw(screen)
        
        for particle in swarm.particles:
            pygame.draw.circle(screen, (0, 0, 255), (particle.x, particle.y), 4)

        pso.update()
        swarm.update(food)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
