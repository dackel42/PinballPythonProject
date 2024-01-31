# Imports
import pygame

class Triangle():
    #creates a triangle
    def __init__(self, screen, color, p1, p2, p3):
        self.screen = screen
        self.color = color 
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    #Bounceboost for the ball when colliding with a triangle
    bounceBoost = 1

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, [self.p1, self.p2, self.p3])
        pygame.draw.circle



    

        