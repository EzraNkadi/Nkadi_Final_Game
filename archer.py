from random import randint
import pygame
from util_params import *
from assets import *
from arrow import *
from player import*
#constants 
ANIMATION_SPEED = 0.15
class Archer(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.frames = ARCHER_FRAMES
        self.image = self.frames[0]
        #create a rect for the archer for future colission checks
        self.rect = self.image.get_rect()
        #create the archer in the middle of the screen for now will randomly generate later
        self.pos = pos
        #create random rate of fire 
        self.fire = randint(1,5)
        #set qualities of animation 
        self.attack_animation_length = 8
        self.animation_speed =  ANIMATION_SPEED
        self.frame_index = 0
        self.time_elapsed = 0.0
        #make it so that the archers do not all shoot at the same time
        self.time_since_shot = randint(0, self.fire)
    def update_archer(self, dt, player_rect):
        """in update attack and animation will be controlled"""
        self.visual_update(player_rect.center)


    def visual_update(self, player_center):
        '''control the archer '''
        #if the x position of the rect of the archer is less than that of the player then it will face right 
        facing_right = player_center.center[0] > self.rect.centerx

        current_frame = self.frames[self.frame_index]
        if facing_right == False:
            self.image = pygame.transform.flip(current_frame, 1, 0)
        else:
            self.image = current_frame




