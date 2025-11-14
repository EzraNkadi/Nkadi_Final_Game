import pygame
from util_params import *
from background import *
from assets import *
####### CONSTANTS ######
TARGET_FRAME_WIDTH = 64
TARGET_FRAME_HEIGHT = 64
PLAYER_SPEED = 5
####### ANIMATION SPEEDS ######
ANIMATION_SPEED_IDLE = 0.15 
ANIMATION_SPEED_RUN = 0.10
ANIMATION_SPEED_ATTACK = 0.05
######## ANIMATION LISTS ######
IDLE_FRAMES = []
RUN_FRAMES = []
ATTACK_FRAMES = []
class Player:
    def __init__(self, idle_frames, run_frames, attack_frames):
        # position and speed
        self.speed = PLAYER_SPEED
        #check that frames were loaded 
        if idle_frames:
            initial_frame = idle_frames[0]
            self.pos_x = (WIDTH//2 - initial_frame.get_width() //2)
            self.pos_y = (WIDTH//2 - initial_frame.get_height() //2)
        else:
            self.pos_x = WIDTH//2
            self.pos_y = HEIGHT//2
        # initialize the animation lists imported fron assets 
        self.idle_frames = IDLE_FRAMES
        self.run_frames = RUN_FRAMES
        self.attack_frames = ATTACK_FRAMES

        # determine which state the player is in 
        self.cirrent_frame_index = 0
        self.time_elapsed = 0
        self.current_animation_speed = ANIMATION_SPEED_IDLE
        self.state = 'idle'

    #update the player
    def update(self, dt, keys):
        '''updates the position of thep player, the animation state, and therefore the animatino of the player'''

        #check for motion

        moved = False
        if keys[pygame.K_LEFT]:
            self.pos_x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT]:
            self.pos_x += self.speed
            moved = True
        if keys[pygame.K_UP]:
            self.pos_y += self.speed
            moved = True
        if keys[pygame.K_DOWN]:
            self.pos_y -= self.speed
            moved = True

        #determine the sate of the plater
        if keys[pygame.K_SPACE] and self.attack_frames:




