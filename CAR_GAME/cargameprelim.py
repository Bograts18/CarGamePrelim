import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("GAME ni BOGART")
clock = pygame.time.Clock()

#Inoput of Backgound:
road = pygame.image.load('roadmap.png')
road_y = -400

side = pygame.image.load('grass1.png')
side_rect = side.get_rect(topleft = (850, -850))
side_x = 850
side_y = -850

undo = pygame.image.load('grass2.png')
undo_rect = undo.get_rect(topleft = (-560,-150))
undo_x = 0
undo_y = -850


#Input of Player/Main Char.:
player = pygame.image.load('carmain.png')
player_rect = player.get_rect(topleft = (510, 400))
player_x = 510
player_y = 400

#Input of Cars:
cr1 = pygame.image.load('car1.png')
cr1_rect = player.get_rect(topleft = (640, -300))
cr1_x = 240
cr1_y = -300

cr2 = pygame.image.load('car2.png')
cr2_rect = player.get_rect(topleft = (530, -400))
cr2_x = 530
cr2_y = -400

cr3 = pygame.image.load('car3.png')
cr3_rect = player.get_rect(topleft = (460, -1500))
cr3_x = 460
cr3_y = -1500

cr4 = pygame.image.load('car4.png')
cr4_rect = player.get_rect(topleft = (280, -2600))
cr4_x = 280
cr4_y = -2600

cr5 = pygame.image.load('car5.png')
cr5_rect = player.get_rect(topleft = (730, -1100))
cr5_x = 730
cr5_y = -1100

cr6 = pygame.image.load('car6.png')
cr6_rect = player.get_rect(topleft = (360, -420))
cr6_x = 360
cr6_y = -420

cr7 = pygame.image.load('car7.png')
cr7_rect = player.get_rect(topleft = (630, -2400))
cr7_x = 630
cr7_y = -2400


#Life Counter:
life = pygame.image.load('heart.png')
life_rect = life.get_rect(topleft = (700, 0))

life1 = pygame.image.load('heart.png')
life1_rect = life1.get_rect(topleft = (750, 0))


#Game Over:
over = pygame.image.load('game over.png')

#Activate:
active = True

#Speed
speed_x = 0
speed_y = 0

#Number Of Lives:
lives = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

        if active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    speed_x = 5

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    speed_x = 0

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    speed_x = -5

            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    speed_x = 0

        else:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    active = True
                    speed_x = 0
                    speed_y = 0
                    player_rect.x = player_x
                    player_rect.y = player_y
                    cr1_rect.y = cr1_y
                    cr2_rect.y = cr2_y
                    cr3_rect.y = cr3_y
                    cr4_rect.y = cr4_y
                    cr5_rect.y = cr5_y
                    cr6_rect.y = cr6_y
                    cr7_rect.y = cr7_y
                    lives = 2

    if active:

        #Background Movement:
        road_y = road_y + 13
        if road_y > 0 : road_y = -600
        screen.blit(road,(200, road_y))

        side_y = side_y + 13
        if side_y > 0 : side_y = -600
        screen.blit(side, side_rect)

        undo_y = undo_y + 13
        if undo_y > 0 : undo_y = -600
        screen.blit(undo, undo_rect)

           
        #Player and Car Movement (code):
        cr1_rect.y += 8
        if cr1_rect.top >= 7000 : cr1_rect.bottom = 0
        screen.blit(cr1, cr1_rect)

        cr2_rect.y += 15
        if cr2_rect.top >= 7000 : cr2_rect.bottom = 0
        screen.blit(cr2, cr2_rect)

        cr3_rect.y += 10
        if cr3_rect.top >= 7000 : cr3_rect.bottom = 0
        screen.blit(cr3, cr3_rect)

        cr4_rect.y += 16
        if cr4_rect.top >= 7000 : cr4_rect.bottom = 0
        screen.blit(cr4, cr4_rect)

        cr5_rect.y += 20
        if cr5_rect.top >= 7000 : cr5_rect.bottom = 0
        screen.blit(cr5, cr5_rect)

        cr6_rect.y += 29
        if cr6_rect.top >= 7000 : cr6_rect.bottom = 0
        screen.blit(cr6, cr6_rect)

        cr7_rect.y +=23
        if cr7_rect.top >= 7000 : cr7_rect.bottom = 0
        screen.blit(cr7, cr7_rect)

        player_rect.x += speed_x
        player_rect.y += speed_y
        screen.blit(player, player_rect)

        for i in range(lives):
            screen.blit(pygame.transform.scale(life, (40, 80)), (700 + i * 50, 0))

        # Showcase of the Collide Fucntion 
        if player_rect.colliderect(cr1_rect) or \
            player_rect.colliderect(cr2_rect) or \
            player_rect.colliderect(cr3_rect) or \
            player_rect.colliderect(cr4_rect) or \
            player_rect.colliderect(cr5_rect) or \
            player_rect.colliderect(cr6_rect) or \
            player_rect.colliderect(cr7_rect) or \
            player_rect.colliderect(side_rect) or \
            player_rect.colliderect(undo_rect):
                    lives -= 1
                    speed_x = 0
                    speed_y = 0
                    player_rect.x = player_x
                    player_rect.y = player_y
                    cr1_rect.y = cr1_y
                    cr2_rect.y = cr2_y
                    cr3_rect.y = cr3_y
                    cr4_rect.y = cr4_y
                    cr5_rect.y = cr5_y
                    cr6_rect.y = cr6_y
                    cr7_rect.y = cr7_y

                    
                    if lives < 0:
                        active = False
                        screen.blit(over, (232,0))


    pygame.display.update()
    clock.tick(60)