import pygame
from util_params import *
from background import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#initialize idle sprite sheet
pygame.init()
#set the ammount of frames that are in the animation 
NUM_FRAMES = 8
IDLE_FRAMES = []
#set the size of the character
TARGET_FRAME_WIDTH = 64
TARGET_FRAME_HEIGHT = 64
for i in range(NUM_FRAMES):
    # loop through range of ammount of frames to get each individual png
    file_path = f'building blocks/warrior_movements/0{i}_Warrior_Idle.png'

    try:
        #load the image and make its background transparent
        frame_image = pygame.image.load(file_path).convert_alpha()
        scaled_frame = pygame.transform.scale(frame_image, (TARGET_FRAME_WIDTH, TARGET_FRAME_HEIGHT) )
        #append the individual pngs to the list to be looped through later
        IDLE_FRAMES.append(scaled_frame)
    except pygame.error as e:
        print(f"failed to load image")
        print(f"pygame error")

        break


