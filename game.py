from util_params import *
import pygame
from background import *
from random import randint
from player import *
# pygame setup
pygame.init()

### Screen Properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True
#call background
background = make_background()
# TESTING ZONE ###############################

current_frame = 0
animation_speed = 0.1
time_elapsed = 0

if IDLE_FRAMES:
    player_pos = (WIDTH//2 - IDLE_FRAMES[0].get_width(), HEIGHT//2 - IDLE_FRAMES[0].get_height())


########################################################################

while running:
    # poll for events
    dt = clock.tick(60)/1000

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_elapsed += dt
    if time_elapsed >= animation_speed:
        current_frame = (current_frame +1) % len(IDLE_FRAMES)
        time_elapsed = 0
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(background,(0,0))
    if IDLE_FRAMES:
        current_image = IDLE_FRAMES[current_frame]
        background.blit(current_image, player_pos)


    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

