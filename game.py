from util_params import *
import pygame
from background import *
from random import randint
from player import *
from score_tracker import *
from assets import *
from start_screen import *
from archer import *
from arrow import *
# pygame setup
pygame.init()

### Screen Properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeon Crawler')
clock = pygame.time.Clock()
running = True


####### INITIALIZATIONS ################################
game_state = INTRO 
game_state_controller = [game_state]   
background = make_background()
player = Player(IDLE_FRAMES,RUN_FRAMES, ATTACK_FRAMES)
score_tracker = ScoreTracker( 50,10)
archer_manager = ArcherManager()
########################################################
while running:

    
    #create a clock/timer to track the ammount of time that has passed
    dt = clock.tick(60)/1000
    game_state = game_state_controller[0]
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_state in [MENU, OVER]:
            game_state = GAME if game_state == MENU else MENU
            game_state_controller[0] = game_state
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_state == GAME:
            game_state_controller[0] = OVER
    #intialize keys for movement
    keys = pygame.key.get_pressed()

    # game already starts in intro 
    if game_state == INTRO:
        #the intro message will fade away once hits zero state changes to menu 
        alpha -= FADE_SPEED
        if alpha <= 0:
            game_state_controller[0] = MENU
    screen.fill(BLACK)
    # Print out respective message for each state
    if game_state == INTRO:
        draw_text("DODGE THE ARROWS", alpha)
    elif game_state == MENU:
        draw_text("CLICK TO START")
    elif game_state == GAME:
        player.update(dt,keys,background)
    #update the score of the tracker
        score_tracker.increase_score(dt)
    #passes through the players rect so archers know where the archer is 
        archer_manager.update(dt, player.rect , player.state, game_state_controller)
    #background
        background = make_background() 
    #draw the score tracker
        score_tracker.draw(background)
    #draw the archesr
        archer_manager.draw(background)
    #draw the player on top of all other surfaces 
        player.draw(background)

        screen.blit(background,(0,0))
    elif game_state == OVER:
        score_tracker.save_score()
        draw_text("GAME OVER\n CLICK TO RESTART")
        # score_tracker.show_scores(screen, WIDTH//2 - 50, 400 )
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

