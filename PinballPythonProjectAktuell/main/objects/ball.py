# Imports
import pygame
import math
#from objects.circle import Circle
#from objects.polygon import Polygon
#from main.main import circle1

###

# global variables 
GRAVITY_X = 0
GRAVITY_Y = 0.3
DT = 1
s_extra_width = 40


class Ball():
    def __init__(self, x, y, screen, radius, color):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = radius
        self.color = color 
        self.vx = 0
        self.vy = 0 
        

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y] , self.radius)

    # Do a collision with the four given mainwalls
    def collision_with_wall(self):
        #  right and left wall
        if self.x + self.radius > (self.screen.get_width() - s_extra_width) or self.x - self.radius < 0:
            self.vx = -self.vx * 0.6
        
        # bottom wall
        if self.y + self.radius > self.screen.get_height():
            if math.isclose(self.vy, 0, abs_tol=0.2):
                self.vy = 0
                self.y = self.screen.get_height() - self.radius
            else:
                self.vy = -self.vy * 0.6
                self.y = self.y + self.vy*DT
        
        # top wall
        if self.y - self.radius < 0:
            self.vy = abs(self.vy) 
            self.y  = self.radius



    # check the closer schnittpunkt before it is to late
    def check_closer_sp(self, circle):
        # Radius of the outer circle
        R = self.radius + circle.radius

        # Situation: Ball is laying on the ground
        if self.vx == 0:
            x = self.x

            x1 = self.x
            y1 = math.sqrt(circle.radius**2-(x-circle.x)**2)

            x2 = self.x
            y2 = -math.sqrt(circle.radius**2-(x-circle.x)**2)

        # Situation: Ball is rolling
        else:
            m = (self.vy/self.vx)
        # line_velocity_vector  = steigung_gerade * (x-self.x) + self.y
        # line_circle = (x+self.x)²+(y+self.y)² = r_hilfskreis²
        
            # Schnittpunkt 1
            x1 = ((m**2*self.x-m*self.y+m*circle.y+circle.x)-math.sqrt(R**2-(m*(self.x-R-circle.x)-self.y+circle.y)*(m*(self.x+R-circle.x)-self.y+circle.y)))/(m**2+1)
            y1 = m*(x1-self.x)+self.y

            # Schnittpunkt 2
            x2 = ((m**2*self.x-m*self.y+m*circle.y+circle.x)+math.sqrt(R**2-(m*(self.x-R-circle.x)-self.y+circle.y)*(m*(self.x+R-circle.x)-self.y+circle.y)))/(m**2+1)
            y2 = m*(x2-self.x)+self.y

        # Abstand zu den Schnittpunkten
        d1 = math.sqrt((x1-self.x)**2 + (y1-self.y)**2)
        d2 = math.sqrt((x2-self.x)**2 + (y2-self.y)**2)

        if d1 < d2:
            return x1, y1
        else:
            x1 = x2
            y1 = y2
            return x1, y1 

    # Do a collision with a Circle
    def collision_circle(self, circle, x1, y1):
        
        # Betrag des Geschwindigkeitsvektors
        betrag_v = math.sqrt(self.vx**2+self.vy**2)

        # abstand ball mit circle
        d_ball_circle = math.sqrt((self.x-circle.x)**2+(self.y-circle.y)**2)
        
        # Collision with the circle if the distance between ball and schnittpunkt is smaller than the betrag of the velocity vector
        
            # projektion des balls, falls in circle
            # wenn ball in circle dann verschiebe ihn auf den schnittpunkt
        if d_ball_circle < circle.radius:
            self.x = x1
            self.y = y1
        # wenn er auf schnittpunkt, dann spiegle den vector
        elif d_ball_circle == circle.radius:  
            betrag_v = math.sqrt(self.vx**2+self.vy**2)
            betrag_w = math.sqrt((circle.x - x1)**2+(circle.y - y1)**2)
            skalar_vw = abs((circle.x - x1)*self.vx+(circle.y - y1)*self.vy)
            winkel_vw = math.acos(skalar_vw/(betrag_v*betrag_w))
            print(winkel_vw)   
         

    # Do a collision with a Polygon 
    def collision_polygon(self):
        pass       

    def cross_poduct(self, a, b):
        return a[0]*b[1]-a[1]*b[0]

            
    # new coordinates of the ball
    def update(self):
        #self.check_closer_sp(circle1)
        #print(self.check_closer_sp(circle1))

        # define velocity 
        if self.vy != 0:
            self.vy = self.vy + GRAVITY_Y*DT
        self.x = self.x + self.vx*DT
        self.y = self.y + self.vy*DT + 0.5*GRAVITY_Y*DT**2

        # first check if collision with wall
        self.collision_with_wall()
    
        # finally draw the ball
        self.draw()
        
    

        