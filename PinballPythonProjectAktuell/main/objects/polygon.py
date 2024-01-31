import pygame

class Polygon():
    #creates a polygon
    def __init__(self, screen, color, point_list):
        self.screen = screen
        self.color = color 
        self.point_list = point_list

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.point_list)
        pygame.draw.circle