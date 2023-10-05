import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("MAV_CAR_GAME")
clock = pygame.time.Clock()

road = pygame.image.load('roadmap.png')
road_y = -600

grass = pygame.image.load('grass.png')
grass_rect = grass.get_rect(topleft = (600, -600))
grass_x = 600
grass_y = -600

flp = pygame.image.load('grass2.png')
flp_rect = flp.get_rect(topleft = (0, -600))
flp_x = 0
flp_y = -600

#mainchar
main = pygame.image.load('carmain.png')
main_rect = main.get_rect(topleft = (460, 400))
main_x = 460
main_y = 400

cr1 = pygame.image.load('car1.png')
cr1_rect = cr1.get_rect(topleft = (240, 0))
cr1_x = 240
cr1_y = 0

cr2 = pygame.image.load('car2.png')
cr2_rect = cr2.get_rect(topleft = (460, -400))
cr2_x = 460
cr2_y = -400

cr3 = pygame.image.load('car3.png')
cr3_rect = cr3.get_rect(topleft = (460, -1500))
cr3_x = 460
cr3_y = -1500

cr4 = pygame.image.load('car4.png')
cr4_rect = cr4.get_rect(topleft = (240, -2600))
cr4_x = 240
cr4_y = -2600

life = pygame.image.load('heart.png')
life_rect = life.get_rect(topleft = (700,0))

life1 = pygame.image.load('heart.png')
life1_rect = life1.get_rect(topleft = (750,0))

over = pygame.image.load('game over.png')

active = True

speed_x = 0
speed_y = 0

lives = 2

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
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
					main_rect.x = main_x
					main_rect.y = main_y
					cr1_rect.y = cr1_y
					cr2_rect.y = cr2_y
					cr3_rect.y = cr3_y
					cr4_rect.y = cr4_y
					lives = 2
   
if active:
	road_y = road_y + 2
	if road_y > 0 : road_y = -600
	screen.blit(road (200, road_y))

	grass_y = grass_y + 2
	if grass_y > 0 : grass_y = -600

	screen.blit(grass, grass_rect)

	flp_y = flp_y + 2
	if flp_y > 0 : flp_y = -600

	screen.blit(flp, flp_rect)

	cr1_rect.y += 4
	if cr1_rect.top >= 7000 : cr1_rect.bottom = 0

	screen.blit(cr1, cr1_rect)

	cr2_rect.y += 4
	if cr2_rect.top >= 7000 : cr2_rect.bottom = 0

	screen.bliy(cr2, cr2_rect)

	cr3_rect.y += 4
	if cr3_rect.top >= 7000 : cr3_rect.bottom = 0

	screen.blit(cr3, cr3_rect)

	cr4_rect.y += 4
	if cr4_rect.top >= 7000 : cr4_rect.bottom = 0

	screen.blit(cr4, cr4_rect)

	main_rect.x += speed_x
	main_rect.y += speed_y

	screen.blit(main, main_rect)

	for i in range(lives):
		screen.blit(pygame.transform.scale(life, (40,80)), (700 + i * 50, 0))
	
	if main_rect.colliderect(cr1_rect) or main_rect.coliiderect(cr2_rect) or main_rect.colliderect(cr3_rect) or main_rect.colliderect(cr4_rect) or main_rect.colliderect(grass_rect) or main_rect.colliderect(flp_rect):
		lives -= 1
		speed_x = 0
		speed_y = 0
		main_rect.x = main_x
		main_rect.y = main_y
		cr1_rect.y = cr1_y
		cr2_rect.y = cr2_y
		cr3_rect.y = cr3_y
		cr4_rect.y = cr4_y

		if lives < 0:
			active = False
			screen.blit(over, (0,0))



pygame.display.update()
clock.tick(60)

    	   



