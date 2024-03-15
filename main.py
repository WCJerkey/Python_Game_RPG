import pygame
from sys import exit
from random import randint

def display_score():
    current_score = int(pygame.time.get_ticks()/100) - start_score
    score_surface = test_font.render(f"Score: {current_score}", False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_score

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            #Rendering Movement
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstecle_rect in obstacles:
            if player.colliderect(obstecle_rect): return False
    return True


pygame.init()
start_score = 0
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake RPG")
clock = pygame.time.Clock()
test_font = pygame.font.Font("./font/Pixeltype.ttf", 50)
game_active = False
score = 0 


sky_surface = pygame.image.load('./graphics/Sky.png').convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()


#Obstacles
snail_surface = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
fly_surface = pygame.image.load("./graphics/Fly/fly1.png").convert_alpha()

obstacle_rect_list = []

player_surface = pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha()
player_rec = player_surface.get_rect(midbottom = (80, 300))


#Intro Screen
player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rec = player_stand_scaled.get_rect(center = (400, 200))

#Intro Screen Text
intro_text = test_font.render("Space Runner", False, "White")
intro_text_rect = intro_text.get_rect(center = (400,80))

intro_text2 = test_font.render("Press ENTER to play", False, "White")
intro_text2_rect = intro_text2.get_rect(center = (400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)



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
                obstacle_rect_list = []
                game_active = True

        if event.type == obstacle_timer and game_active:    
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))

    if game_active:
        #Drawing Environment
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        #Player
        player_gravity += 0.5
        player_rec.y += player_gravity
        if player_rec.bottom > 300: player_rec.bottom = 300
        screen.blit(player_surface, player_rec)

        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rec, obstacle_rect_list)

    else:
        screen.fill("Black")
        screen.blit(player_stand_scaled, player_stand_rec)

        #Score
        score_surface = test_font.render(f"Your Score: {score}", False, "White")
        score_surface_rect = score_surface.get_rect(center = (400,320))

        screen.blit(intro_text, intro_text_rect)
        
        if score == 0:
            screen.blit(intro_text2, intro_text2_rect)
        else:
            screen.blit(score_surface, score_surface_rect)


    pygame.display.update()
    clock.tick(60)