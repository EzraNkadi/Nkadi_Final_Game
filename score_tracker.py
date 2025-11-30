import pygame
import json
filename = 'scores.json'
#create a class for the score 
class ScoreTracker: 
    #takes input for size position and color
    def __init__(self, x, y, font_size = 36, color = (255,255,255)):
        self.score = 0
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = None
        self.score_saved = False
        self.update_surface()

        #create a way to update score
        #score will end up being updated after time passes
    def increase_score(self, dt):
        self.score += dt 
        self.update_surface()

    def update_surface(self):
        '''writes the score onto a surface'''
        text = f"score: {int(self.score)}"
        self.text_surface = self.font.render(text, True, self.color)
        
    #method to draw the score onto the screen 
    #Add the score to the scores.txt file
    def save_score(self):
        #makes it so that only runs once therefore only saving the new score once 
        if self.score_saved == True:
            return
        #will sort the list and keep only the top 3 scores
        current_score = int(self.score)
        with open(filename, 'w') as file:
            #load the score into the json file
            json.dump(current_score, file)
        self.score_saved = True

    def draw(self, background):
        background.blit(self.text_surface, (self.x, self.y))     
