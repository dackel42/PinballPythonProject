import pygame
import math

class Circle():
    def __init__(self, x, y, screen, radius, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)