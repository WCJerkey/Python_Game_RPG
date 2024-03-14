import pygame
from sys import exit

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake RPG")
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 50)


sky_surface = pygame.image.load('./graphics/Sky.png').convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()
text_surface = test_font.render("My Game", False, "Black").convert()


snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_rec = player_surface.get_rect(midbottom = (80, 300))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    snail_rec.right -= 4
    player_rec.right += 1
    if snail_rec.right <= 0: snail_rec.left = 800

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, snail_rec)
    screen.blit(player_surface, player_rec)


    pygame.display.update()
    clock.tick(60)