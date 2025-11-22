import pygame
from util_params import *
from background import *
from assets import *
from math import *
####### CONSTANTS ######
TARGET_FRAME_WIDTH = 64
TARGET_FRAME_HEIGHT = 64
PLAYER_SPEED = 5
PLAYER_WATER_SPEED = 2.5
####### ANIMATION SPEEDS ######
ANIMATION_SPEED_IDLE = 0.1
ANIMATION_SPEED_RUN = 0.1
ANIMATION_SPEED_ATTACK = 0.05
######## ANIMATION LISTS ######
IDLE_FRAMES = []
RUN_FRAMES = []
ATTACK_FRAMES = []

class Player:
    def __init__(self, IDLE_FRAMES, RUN_FRAMES, ATTACK_FRAMES):
# position and speed changes at set speed
        self.speed_x = PLAYER_SPEED
        self.speed_y = PLAYER_SPEED
#check that frames were loaded 
        if IDLE_FRAMES:
            #if IDLE_FRAMES is true meaning the images were loaded then create position of player
            initial_frame = IDLE_FRAMES[0]
            self.pos_x = (WIDTH//2 - initial_frame.get_width() //2)
            self.pos_y = (WIDTH//2 - initial_frame.get_height() //2)

            w = 32
            h = 32
            # initialize the animation lists imported fron assets 
        self.idle_frames = IDLE_FRAMES
        self.run_frames = RUN_FRAMES
        self.attack_frames = ATTACK_FRAMES

        #create a theta for player turning 
        self.theta = 0

        # determine which state the player is in setting default as idle 
        self.current_frame_index = 0
        self.time_elapsed = 0.0
        self.current_animation_speed = ANIMATION_SPEED_IDLE
        self.state = 'idle'
        
        self.rect = pygame.Rect(0, 0, w , h )
        self.rect.center = (self.pos_x + 2//2, self.pos_y + h//2)
#update the player
    def update(self, dt, keys, background):
        '''updates the position of thep player, the animation state, and therefore the animatino of the player'''
        #create position at the center of character

        # self.center_x = int(self.pos_x + TARGET_FRAME_WIDTH /2)
        # self.center_y = int(self.pos_y + TARGET_FRAME_HEIGHT /2)
        # #to slow down character check if is in water
        # #check the pixel color of what is behind the player to determine if in water
        # self.pixel_color = background.get_at((self.center_x, self.center_y))
        # #check the R G B value, since the water is blue that is third index of tuple
        # self.is_in_water = self.pixel_color[2]>200 and self.pixel_color[1] >100
        # print(self.pixel_color)
        # if self.is_in_water:
        #     self.speed = 2.5
        # else:
        #     self.speed = 5.0
        
    # need to find the change in distance for rotation    
    #check for motion
        current_speed = PLAYER_SPEED


        moved = False
        if keys[pygame.K_LEFT]:
            self.pos_x  -= current_speed
        moved = True
        if keys[pygame.K_RIGHT]:
            self.pos_x += current_speed
        moved = True
        if keys[pygame.K_UP]:
            self.pos_y -= current_speed
        moved = True
        if keys[pygame.K_DOWN]:
            self.pos_y += current_speed
        moved = True
        w = 64
        h = 64
        #draw the rectangle at the center of the player
        #move the rectangle where the playe is moving
        self.rect.center = (self.pos_x + w//2 , self.pos_y + h//2)
#determine the sate of the plater
        if keys[pygame.K_SPACE]: 
            #reset the frame if not in attack state
            if self.state != 'attack':
                self.current_frame_index = 0
            #if space is being pressed 
            self.state = 'attack'
            self.current_animation_speed = ANIMATION_SPEED_ATTACK
        #if space is not being pressed but are moving
        elif moved:
            self.state = 'run'
            self.current_animation_speed = ANIMATION_SPEED_RUN
        #if you are not moving and space not being pressed 
        elif self.idle_frames:
            self.state = 'idle'
            self.current_animation_speed = ANIMATION_SPEED_IDLE

        #time tracker
        self.time_elapsed += dt
        #checks to see if enough time has passed for the current animation state
        if self.time_elapsed >= self.current_animation_speed:
            #if is true the time elapsed gets reset to reset the timer and continue the animation
            self.time_elapsed = 0
        
        

#select the frame list 
            frames = []
            #changes the frames to RUN_FRAMES list
            if self.state == 'run':
                frames = self.run_frames
            #changes the frames to ATTACK_FRAMES list
            elif self.state =='attack':
                frames = self.attack_frames
            #changes the frames to IDLE_FRAMES list
            else:
                frames = self.idle_frames

            if frames:
                self.current_frame_index = (self.current_frame_index +1) % len(frames)

    #if in attack state, stop animation of the last frame, checks that the last frame was last frame of animation
                if self.state == 'attack' and self.current_frame_index == 0:
                    self.current_frame_index = len(self.attack_frames) - 1
                    #resets animation state to idle
                    self.state = 'idle'
    #draw the player onto the background
    def draw(self, background):
        """draw the player onto the background """
        #frame list for animation
        frames = []
        #determine what is inside of the frame list based off of player state
        if self.state =='run':
            frames = self.run_frames
        elif self.state =='attack':
            frames = self.attack_frames
        else:
            frames = self.idle_frames
        # if there are values in the frame list draw the player
        if frames:
            current_image = frames[self.current_frame_index]
            #draw the rectangle to make sure it is in the correct position will remove later
            pygame.draw.rect(background, (255,255,0), self.rect, 1)
            current_image = pygame.transform.rotozoom(current_image,0.0 ,1)
            background.blit(current_image, (self.pos_x, self.pos_y))








