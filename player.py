import pygame
from util_params import *
from background import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#initialize idle sprite sheet
pygame.init()
#set the ammount of frames that are in the animation 
keys = pygame.key.get_pressed()
#set the size of the character
TARGET_FRAME_WIDTH = 64
TARGET_FRAME_HEIGHT = 64
#create animation for running 
NUM_FRAMES_RUN = 6
RUN_FRAMES = []
#same process as for idle animation, add seperate variable for ammount of frames and a seperate list for png's
for i in range(NUM_FRAMES_RUN):
    run_file = f'building blocks/warrior_movements/0{i}_Warrior_Run.png'

    try:
        frame_image_run = pygame.image.load(run_file).convert_alpha()
        run_scaled = pygame.transform.scale(frame_image_run, (TARGET_FRAME_WIDTH, TARGET_FRAME_HEIGHT) )


        RUN_FRAMES.append(run_scaled)
    except pygame.error as e:
        print(f"something in the code is not working")

NUM_FRAMES = 8
IDLE_FRAMES = []
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


    

