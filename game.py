from util_params import *
import pygame
from background import *
from random import randint
from player import *
from score_tracker import *
from assets import *
from start_screen import *
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
             pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_state in [MENU, OVER]:
            game_state = GAME if game_state == MENU else MENU
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_state == GAME:
            game_state = OVER
    #intialize keys for movement
    keys = pygame.key.get_pressed()

    # game already starts in intro 
    if game_state == INTRO:
        #the intro message will fade away once hits zero state changes to menu 
        alpha -= FADE_SPEED
        if alpha <= 0:
            game_state = MENU
    screen.fill(BLACK)
    # Print out respective message for each state
    if game_state == INTRO:
        draw_text("DODGE THE ARROWS", alpha)
    elif game_state == MENU:
        draw_text("CLICK TO START")
    elif game_state == GAME:
        screen.blit(background,(0,0))
    elif game_state == OVER:
        draw_text("GAME OVER")
        #update the player 
    player.update(dt,keys)
    # create the background 
    background = make_background()
    #draw the score tracker 
    score_tracker.draw(background)
    #draw the player on top of all other surfaces 
    player.draw(background)
       
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

