from dimensions_utils import *
import pygame
from background import *
from random import randint
# pygame setup
pygame.init()

### Screen Properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True

#call background
background = make_background()

########################## TESTING ZONE ###############################



########################################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(background,(0,0))
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

