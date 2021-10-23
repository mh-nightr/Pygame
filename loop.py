### This code holds the very basic game loop to run a window in Pygame ###

import pygame, sys

## Game Loop ##
pygame.init()
clock = pygame.time.Clock()

# Setting up window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

while True:
	# Handling input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	# Updating the window 
	pygame.display.flip()
	clock.tick(60)