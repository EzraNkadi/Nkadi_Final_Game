from random import randint
import pygame
from util_params import *
from math import *
#create a class for the arrows
class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        #create a targeting relative to the position of the player and the starting position of the arrow
        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]
        distance = sqrt(dx**2+dy**2)
        self.ARROW_SPEED = 7
        #if the arrow gets to target position it gets killed
        if distance == 32:
            self.kill()
            return
        #x and y velocity
        self.vel_x = (dx/distance)* self.ARROW_SPEED
        self.vel_y = (dy/distance)* self.ARROW_SPEED
        #load the arrow image 
        self.image = pygame.image.load('building blocks/archer_movements/Arrow.png')
        theta = atan2(-dy, dx)
        degrees = theta *(180/pi)
        self.image = pygame.transform.rotozoom(self.image, degrees, 0.5 )
        self.rect = self.image.get_rect(center=start_pos)
        #update the arrow 
    def update(self, dt):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        #if the arrow goes off of the screen remove it from the spritegroup
        if self.rect.right < -50 or self.rect.left > WIDTH+50 or self.rect.bottom < -50 or self.rect.top > HEIGHT+50:
            self.kill()
        



