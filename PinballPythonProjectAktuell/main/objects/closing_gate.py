import pygame
import math

class ClosingGate():
    def __init__(self, screen, color, p1, p2, p3, p4, rotation_center, min_angle, max_angle):
        self.screen = screen
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.point_list = [self.p1, self.p2, self.p3, self.p4]
        self.rotation_center = rotation_center
        self.rotation_speed = 0.02
        self.rotation_angle = min_angle
        self.close_signal = False
        self.open_signal = False
        self.min_angle = min_angle
        self.max_angle = max_angle

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.point_list)
    
    def start_signal(self):
        self.close_signal = True
        self.rotation_speed = abs(self.rotation_speed)

    def reset_signal(self):
        self.open_signal = True
        self.rotation_speed = -abs(self.rotation_speed)

    def move_gate(self):
        list_index = 0
        if  self.close_signal == True:
            if self.point_list[2][0] >= 605:
                self.close_signal = False
            else:
                for coordinate in self.point_list:
                    coordinate_x = self.rotation_center[0] + (coordinate[0] - self.rotation_center[0]) * math.cos(self.rotation_speed) - (coordinate[1] - self.rotation_center[1]) * math.sin(self.rotation_speed)
                    coordinate_y = self.rotation_center[1] + (coordinate[0] - self.rotation_center[0]) * math.sin(self.rotation_speed) + (coordinate[1] - self.rotation_center[1]) * math.cos(self.rotation_speed)
                    self.point_list[list_index] = coordinate_x, coordinate_y
                    list_index += 1
        
        elif self.open_signal == True:
            if self.point_list[2][1] >= 150:
                self.open_signal = False
            else:
                for coordinate in self.point_list:
                    coordinate_x = self.rotation_center[0] + (coordinate[0] - self.rotation_center[0]) * math.cos(self.rotation_speed) - (coordinate[1] - self.rotation_center[1]) * math.sin(self.rotation_speed)
                    coordinate_y = self.rotation_center[1] + (coordinate[0] - self.rotation_center[0]) * math.sin(self.rotation_speed) + (coordinate[1] - self.rotation_center[1]) * math.cos(self.rotation_speed)
                    self.point_list[list_index] = coordinate_x, coordinate_y
                    list_index += 1
        self.draw()
