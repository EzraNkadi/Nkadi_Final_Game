import pygame
from util_params import *
from background import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#initialize idle sprite sheet
idle = pygame.image.load('building blocks/Warrior/Warrior_Idle.png')
idles = []
idle_width = idle.get_width()
idle_height = idle.get_height()
idle_cols = idle_width // TILE_SIZE
idle_rows = idle_height // TILE_SIZE
for y in range (idle_rows):
    for x in range (idle_cols):
        idles.append(get_tile(idle, x, y))


class Player(pygame.sprite.Sprite):
    def __init__(self,x, y, animation_list):
        super().__init__()
        self.idle_frames = animation_list

        self.current_frame = 0
        self.image = self.idle_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        #control the speed of going through the list 
        self.animation_speed = 0.15
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        #check how much time has passed if it has been enough to go to new picture
        if now - self.last_update > self.animation_speed *1000:
            self.last_update = now
            #move to the next frame if at the end of the list go to the beginning
            self.current_frame = (self.current_frame +1) % len(self.idle_frames)
            self.image = self.idle_frames[self.current_frame]
