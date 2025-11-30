from random import randint
import pygame
from util_params import *
from assets import *
from arrow import *
from player import*
from arrow import *
#sound 
pygame.mixer.init()
sound_hit = pygame.mixer.Sound('building blocks/impactBell_heavy_000.ogg')
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
        self.fire_rate = randint(1,5)
        self.time_since_shot = randint(0, self.fire_rate)
        #set qualities of animation same as use dwith player
        self.attack_animation_length = 8
        self.animation_speed =  ANIMATION_SPEED
        self.frame_index = 0
        self.time_elapsed = 0.0
        #set the attacking as false when archer is first spawned
        self.attacking = False
    #function to make it so that arrows shoot 
    def shoot_arrow(self, target_pos, arrow_group):
            new_arrow = Arrow(self.rect.center, target_pos)
            arrow_group.add(new_arrow)
    #add the arrow group to the update method to control the arrows 
    def update(self, dt, player_rect, arrow_group):
        #if the archer is not in the not animating
        if self.attacking == False:
            #adds time to the shot timer 
            self.time_since_shot += dt
            #if the time that has passed reached the shot cooldown then start the animation for the archer 
            if self.time_since_shot >= self.fire_rate:
                self.attacking = True
                #reset the time since shot 
                self.time_since_shot = 0
                self.frame_index = 0
        #make it so that anmation loop only runs if the archer is attacking
        if self.attacking == True:
            #timer for the animation 
            self.time_elapsed += dt
            #if enough time has passed go to the next frame 
            if self.time_elapsed >= self.animation_speed:
                self.time_elapsed = 0
                self.frame_index += 1
                #check to see if the animation is complete
                if self.frame_index >= self.attack_animation_length:
                    #at the end of each animation cycle an arrow gets shot
                    self.shoot_arrow(player_rect.center, arrow_group)
                    #animation state/attack state gets reset 
                    self.attacking = False
                    self.frame_index = 0
                    self.image = self.frames[0]
                else:
                    #where the new image is actually updated 
                    self.image = self.frames[self.frame_index]
        else:
            self.image = self.frames[0]


        #flipping update after each frame has been loaded
        self.visual_update(player_rect.center)
        
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
        self.arrows = pygame.sprite.Group()
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
    def update(self, dt, player_rect, player_state, game_state_controller):
        #update all of the archers
        self.archers.update(dt, player_rect, self.arrows)
        self.arrows.update(dt)
        #check for arrow collission with player
        arrow_hit_player = False
        #repeats for the ammount of arrows currently present
        for arrow in self.arrows:
            #if the player collides with the arrow rect
            if player_rect.colliderect(arrow.rect):
                arrow_hit_player = True
                sound_hit.play()
                arrow.kill() 
                break
        #once the variable turns true after making contact with player rect this will run 
        if arrow_hit_player == True:
            #will bring the game to the gameover screen
            game_state_controller[0] = OVER
            return
            

    def draw(self, background):
        #draw all archers
        self.archers.draw(background)
        self.arrows.draw(background)




