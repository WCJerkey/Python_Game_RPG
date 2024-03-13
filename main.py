import pygame
from sys import exit

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake RPG")
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)