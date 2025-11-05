from util_params import *
import pygame
from background import *
from random import randint
from player import *
from score_tracker import *
# pygame setup
pygame.init()

### Screen Properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True
#call background
background = make_background()

####ANIMATION####
#set a base frame for reference when going through the list 
current_frame = 0
#create a variable for animation speed so that it can be changed 
animation_speed = 0.2
#variable to track the ammount of time that has been passed 
time_elapsed = 0
if IDLE_FRAMES:
    player_pos_x= (WIDTH//2 - IDLE_FRAMES[0].get_width())
    player_pos_y = (HEIGHT//2 - IDLE_FRAMES[0].get_height())
###################
player_speed = 5


# TESTING ZONE ###############################

score_tracker = ScoreTracker(50,10)

########################################################################

while running:
    # poll for events
    #create a clock/timer to track the ammount of time that has passed
    dt = clock.tick(60)/1000
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #initialize background in loop so that the character 
    # has something taht blits over it so there is no after image
    background = make_background()
    #draw the score tracker 
    score_tracker.draw(background)
    #add the time that has passed to tracker
    time_elapsed += dt
    #go through the indices of the list creating the animation 
    if time_elapsed >= animation_speed:
        current_frame = (current_frame +1) % len(IDLE_FRAMES)
        time_elapsed = 0
    #blit the image onto the background
    if IDLE_FRAMES:
        current_image = IDLE_FRAMES[current_frame]
        background.blit(current_image, (player_pos_x, player_pos_y))
    screen.blit(background,(0,0))
    keys = pygame.key.get_pressed()
    #create movement
    if keys[pygame.K_LEFT]:
        player_pos_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos_x += player_speed
    if keys[pygame.K_UP]:
        player_pos_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos_y += player_speed

    # RENDER YOUR GAME HERE
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

