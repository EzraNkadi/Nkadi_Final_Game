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
        self.rect = self.image.get_rect(topleft = pos)
        #create the archer in the middle of the screen for now will randomly generate later
        self.pos = pos
        #create random rate of fire 
        self.fire = randint(1,5)
        #set qualities of animation same as use dwith player
        self.attack_animation_length = 8
        self.animation_speed =  ANIMATION_SPEED
        self.frame_index = 0
        self.time_elapsed = 0.0
    def update(self, dt, player_rect):
        self.time_elapsed += dt
        #animation loop
        if self.time_elapsed >= self.animation_speed:
            self.time_elapsed = 0

            self.frame_index = (self.frame_index +1) % len(self.frames)
            self.image = self.frames[self.frame_index]
        #flipping update after each frame has been loaded
        self.visual_update(player_rect.center)

        #make it so that the archers do not all shoot at the same time
        #self.time_since_shot = randint(0, self.fire)
    # def update_archer(self, dt, player_rect):
    #     """in update attack and animation will be controlled"""
    #     self.visual_update(player_rect.center)


    def visual_update(self, player_center):
        '''control the archer '''
        #if the x position of the rect of the archer is less than that of the player then it will face right 
        facing_right = player_center[0] > self.rect.centerx

        current_frame = self.frames[self.frame_index]
        #if not faicing right the image will be flipped
        if facing_right == False:
            self.image = pygame.transform.flip(current_frame, 1, 0)
        else:
            self.image = current_frame
##########################################
#class to spawn archer and manage them 
class ArcherManager:
    def __init__(self, spawn_count = 7):
        #pygame sprite group for archer
        self.archers = pygame.sprite.Group()
        #spawns as many archers as in spawn count
        for s in range(spawn_count):
            self.spawn_archer()

    def spawn_archer(self):
        #the position of the archers are randomly generated
        pos_x = randint(0, WIDTH-50)
        pos_y = randint(0, HEIGHT-50)
        #the archer will be created at the randomposition
        new_archer = Archer((pos_x, pos_y))
        #add the new archer to the group
        self.archers.add(new_archer)
    def update(self, dt, player_rect):
        #update all of the archers
        self.archers.update(dt, player_rect)

    def draw(self, background):
        #draw all archers
        self.archers.draw(background)




