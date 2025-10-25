
import pygame
from background import *
from random import randint
# pygame setup
pygame.init()

### Screen Properties
WIDTH = 800
HEIGHT = 608

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True

# background building blocks
basic_floor = floors[1]
wall_bottom = floors[55]
wall_top = floors[19]
wall_left = floors[18]
wall_right = floors[20]
right_corner = floors[27]
left_corner = floors[29]
blank = floors[62]
torches = pygame.image.load('items/torch_4.png')
########################## TESTING ZONE ###############################
###### make a background 



########################################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for x in range (0, WIDTH, TILE_SIZE):
        for y in range(0,HEIGHT, TILE_SIZE):
            screen.blit(basic_floor, (x,y))
    for x in range(0, WIDTH, TILE_SIZE):
        screen.blit(wall_bottom,(x,HEIGHT-58))
    for x in range(0, WIDTH, TILE_SIZE):
        screen.blit(wall_top, (x,0))
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.blit(wall_right,(x,y))
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.blit(wall_left, (0,y))
    for x in range(0,WIDTH, TILE_SIZE):
        for y in range(HEIGHT-54, HEIGHT, TILE_SIZE):
            screen.blit(blank,(x,y))
    for x in range(64, WIDTH - 64, 32):
        for y in range (64, HEIGHT - 64, 32 ):
            screen.blit(torches,(x, y))
   
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

