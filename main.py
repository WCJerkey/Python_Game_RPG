import pygame
from sys import exit

def display_score():
    current_score = int(pygame.time.get_ticks()/100) - start_score
    score_surface = test_font.render(f"Score: {current_score}", False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)

pygame.init()
start_score = 0
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake RPG")
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 50)
game_active = True


sky_surface = pygame.image.load('./graphics/Sky.png').convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()

snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha()
player_rec = player_surface.get_rect(midbottom = (80, 300))

player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand_rec = player_stand.get_rect(midbottom = (400, 300))

player_gravity = 0



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rec.collidepoint(event.pos): player_gravity = -15
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rec.bottom >= 300:
                player_gravity = -15
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_score = int(pygame.time.get_ticks()/100)
                snail_rec.left = 800
                game_active = True

    if game_active:
        #Drawing Environment
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        display_score()
    
        

        #Snail
        snail_rec.right -= 4
        if snail_rec.right <= 0: snail_rec.left = 800
        
        screen.blit(snail_surface, snail_rec)

        #Player
        player_gravity += 0.5
        player_rec.y += player_gravity
        if player_rec.bottom > 300: player_rec.bottom = 300
        screen.blit(player_surface, player_rec)

        #Collision
        if snail_rec.colliderect(player_rec):
            game_active = False
    else:
        screen.fill("Black")
        screen.blit(player_stand, player_stand_rec)


    pygame.display.update()
    clock.tick(60)