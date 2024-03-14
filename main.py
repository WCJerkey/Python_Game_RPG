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


score_surface = test_font.render("My Game", False, (64,64,64)).convert()
score_rect = score_surface.get_rect(center = (400, 50))


snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_rec = player_surface.get_rect(midbottom = (80, 300))

player_gravity = 0



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rec.collidepoint(event.pos): player_gravity = -15
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -15


    #Drawing Environment
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    

    #Snail
    snail_rec.right -= 4
    player_rec.right += 1
    if snail_rec.right <= 0: snail_rec.left = 800
    
    screen.blit(snail_surface, snail_rec)

    #Player
    player_gravity += 0.5
    player_rec.y += player_gravity
    screen.blit(player_surface, player_rec)


    pygame.display.update()
    clock.tick(60)