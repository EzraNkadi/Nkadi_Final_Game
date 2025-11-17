import pygame
import sys
from util_params import *
# variables 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INTRO = 0
MENU = 1
GAME = 2
OVER = 3
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_state = INTRO
alpha = 255
FADE_SPEED = 3

# create the text and blit the text onto the screen 
def draw_text(text, alpha=255, size=80):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, WHITE)
    text.set_alpha(alpha)
    screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))