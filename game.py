from util_params import *
import pygame
from background import *
from random import randint
from player import *
from score_tracker import *
from assets import *
# pygame setup
pygame.init()

### Screen Properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True


####### INITIALIZATIONS ################################
background = make_background()
player = Player(IDLE_FRAMES, RUN_FRAMES, ATTACK_FRAMES)
score_tracker = ScoreTracker(50,10)
########################################################


while running:
    #create a clock/timer to track the ammount of time that has passed
    dt = clock.tick(60)/1000
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #intialize keys for movement
    keys = pygame.key.get_pressed()
    #update the player 
    player.update(dt,keys)
    # create the background 
    background = make_background()
    #draw the score tracker 
    score_tracker.draw(background)
    #draw the player on top of all other surfaces 
    player.draw(background)
    ###################### moving animation ############################3
    screen.blit(background,(0,0))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

