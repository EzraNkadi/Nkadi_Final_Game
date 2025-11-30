import pygame
import json

#create a class for the score 
class ScoreTracker: 
    #takes input for size position and color
    filename = 'scores.json'
    highscores = []
    def __init__(self, x, y, font_size = 36, color = (255,255,255)):
        self.score = 0
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = None
        self.score_saved = False
        self.update_surface()

        if ScoreTracker.highscores == False:
            ScoreTracker.highscores = self.load_scores()
        #create a way to update score
        #score will end up being updated after time passes
    def load_scores(self):
            #uses the json file to read the scores which have been uploaded
            with open(self.filename, 'r') as file:
                scores = json.load(file)
                scores =[s for s in scores]
                #sort the scores from highest to lowest
                scores.sort(reverse = 1)
                #takes only the first three scores 
                return scores[:3]
    #how to save the scores to the json file
    def save_scores_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(ScoreTracker.highscores, file)

    #increases the score as a function of time           
    def increase_score(self, dt):
        self.score += dt 
        self.update_surface()
    #puts messages onto screen 
    def update_surface(self):
        '''writes the score onto a surface'''
        text = f"score: {int(self.score)}"
        self.text_surface = self.font.render(text, True, self.color)

    def save_score(self):
        #makes it so that only runs once therefore only saving the new score once 
        if self.score_saved == True:
             return
        #make the scores into integers
        current_score = int(self.score)
        #add to the list and sort the thist 
        ScoreTracker.highscores.append(current_score)
        ScoreTracker.highscores.sort(reverse = 1)
        ScoreTracker.highscores = ScoreTracker.highscores[:3]
        #writes the sorted list to the json file 
        self.save_scores_to_file()
        #flag changes so that only runs once 
        self.score_saved = True

    def draw(self, background):
        background.blit(self.text_surface, (self.x, self.y))   
        #where the score gets loaded and blit onto screen 
    def show_scores(self, background, x, y, font_size = 40):
        score_font = self.font
        #coordinates 
        y = y
        x = x
        #create surface 
        message = score_font.render("TOP 3 SCORES!!!!!", 1, (0,155,155))
        background.blit(message, (x,y))  
        y += 50
        #goes through the list, enumerate gives the score and index
        for i, score in enumerate(ScoreTracker.highscores):
            rank = i + 1
            text = f"{rank}. {score}"
            
            #Highlight the current score if it was just achieved
            color = (0, 255, 0) if score == int(self.score) and self.score_saved else (255, 255, 255)
            #render the score into a surface and blit it 
            score_surf = score_font.render(text, True, color)
            background.blit(score_surf, (x + 20, y))
            y += 40


