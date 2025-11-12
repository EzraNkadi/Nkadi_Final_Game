import pygame 
from util_params import *
SCREEN_TITLE = "DEADLY DUNGEON"
class DeadlyDungeon:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Dungeon Crawler')
        clock = pygame.time.Clock()

