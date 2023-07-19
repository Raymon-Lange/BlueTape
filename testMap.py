import pygame, sys
from titledLevel import Level
vertical_tile_number = 20
tile_size = 16 

screen_height = vertical_tile_number * tile_size
screen_width = 600

level_0 = {
		'terrain': 'levels/levels/0/level_0_terrain.csv',
		'fruits': 'levels/levels/0/level_0_fruits.csv',
		'player': 'levels/levels/0/level_0_player.csv'}

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen_height, screen_width)



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('grey')
	level.draw(screen, 0)

	pygame.display.update()
	clock.tick(60)