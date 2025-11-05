import pygame
from util_params import *
from background import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#initialize idle sprite sheet
pygame.init()


NUM_FRAMES = 8
IDLE_FRAMES = []
TARGET_FRAM_WIDTH = 64
TARGET_FRAME_HEIGHT = 64
for i in range(NUM_FRAMES):

    file_path = f'building blocks/warrior_movements/0{i}_Warrior_Idle.png'

    try:

        frame_image = pygame.image.load(file_path).convert_alpha()
        scaled_frame = pygame.transform.scale(frame_image, (TARGET_FRAM_WIDTH, TARGET_FRAME_HEIGHT) )
        IDLE_FRAMES.append(scaled_frame)
    except pygame.error as e:
        print(f"failed to load image")
        print(f"pygame error")

        break

