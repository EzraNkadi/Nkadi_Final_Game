##########!!!!!!! MAKE INTO CLASS FOR EFFICIENCY
import pygame
from util_params import *
### Screen Properties
background = pygame.Surface((WIDTH, HEIGHT))

image = pygame.image.load('building blocks/pygame_background.png')
def make_background():
    background.blit(image,(0,0))

    return background
   