import pygame
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
        self.update_surface()


        #create a way to update score
        #score will end up being updated after time passes
    def increase_score(self, dt):
        self.score += int(dt)
        self.update_surface()

    def update_surface(self):
        '''writes the score onto a surface'''
        text = f"score: {self.score}"
        self.text_surface = self.font.render(text, True, self.color)
        
    #method to draw the score onto the screen 
    def draw(self, background):
        background.blit(self.text_surface, (self.x, self.y))        
