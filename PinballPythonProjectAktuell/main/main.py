import math
import pygame
import sys

from objects.ball import Ball 
from objects.triangle import Triangle
from objects.polygon import Polygon
from objects.closing_gate import ClosingGate
from objects.circle import Circle

# Initialize PyGame
pygame.init()

# Initial window size
s_width = 640
s_height = 800

# Define spacetime 
GRAVITY_X = 0.0
GRAVITY_Y = 0.3
DT = 1 # ms (discretization of time) 


# Farben
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)

# Making display screen
screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
bg_orig = pygame.Surface((s_width, s_height), pygame.RESIZABLE)
bg_orig.fill(BLACK)
clock = pygame.time.Clock()

# Setup 
running = True

# Startwerte
ball_startposition_x = 620
ball_startposition_y = 790
# Startbeschleunigung des Balls
starbeschleunigung_ball_max = -40 


# You could declarecomponents (the initial ball, the other items, ...) here
power_triangle_left = Triangle(screen = screen, 
                    color = PURPLE,  
                    p1 = [80, 400], 
                    p2 = [170, 610], 
                    p3 = [80, 560])

power_triangle_right = Triangle(screen = screen, 
                    color = (100, 0, 100),  
                    p1 = [520, 400], 
                    p2 = [430, 610], 
                    p3 = [520, 560])

gameball = Ball(x=ball_startposition_x,
                y=ball_startposition_y,
                screen=screen, 
                radius=10, 
                color=(200,200,200)) 

test_gameball = Ball(x=200,
                y=200,
                screen=screen, 
                radius=10, 
                color=(200,200,200))

first_collision_trinangle = Polygon(screen, 
                                    RED,
                                    [(640,0),
                                     (580,0),
                                     (640,60)])

# Closing gate
gate = ClosingGate(screen, 
                       WHITE,
                       p1=(595,80),
                       p2=(595,150),
                       p3=(585,150),
                       p4=(585,80),
                       rotation_center=(595,80),#
                       min_angle = 0,
                       max_angle = 180)

# Testcircle top right
circle1 = Circle(x=635,
                 y=20,
                 screen=screen,
                 radius=20,
                 color=WHITE)

# Spielfeldbegrenzung
polygon_unten = ((0,800),(0,625),(175,725),(175,800),(425,800),(425,725),(600,625),(600,800))
outerline_coords = ((600,0),(0,0),(0,800),(600,800),(600,80))

# which status
ball_release = False

# Main event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Get's all the user action (keyboard, mouse, joysticks, ...)
        # Start sequence
        if gameball.vy == 0 and gameball.x == ball_startposition_x:
            if event.type == pygame.KEYDOWN: #keydown
                if event.key == pygame.K_SPACE: 
                    space_start = pygame.time.get_ticks()       
            if event.type == pygame.KEYUP: #keyup
                if event.key == pygame.K_SPACE:
                    space_end = pygame.time.get_ticks() 
                    if space_end - space_start <= 2000:
                        beschleunigungs_faktor = (space_end-space_start)/2000
                        starbeschleunigung_ball = beschleunigungs_faktor * starbeschleunigung_ball_max
                    else: 
                        starbeschleunigung_ball = starbeschleunigung_ball_max
                    gameball.vy = starbeschleunigung_ball + GRAVITY_Y*DT
                ball_release = True

        # ball is out start a new round
        if gameball.y <= 790 and gameball.x <= 600:
            ball_release = False
            ####

            # delete old ball
            gameball.delete()
            # create new gameball
            gameball = Ball(x=ball_startposition_x,
                y=ball_startposition_y,
                screen=screen, 
                radius=10, 
                color=(200,200,200)) 
            # reset gate
        ###
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                gate.reset_signal()

        # Close the gate
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                gate.start_signal()
    gate.move_gate()

        # Left Paddle
                
        # Right Paddle
                 
    '''# Adjust screen size
    if event.type == pygame.VIDEORESIZE:
        s_width, s_height = event.size
        screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
        bg = pygame.transform.scale(bg_orig, (s_width, s_height))
        screen.blit(bg, (0, 0))''' 

             
     
    # Adjust screen 
    s_width, s_height = screen.get_width(), screen.get_height()
    bg = pygame.transform.scale(bg_orig, (s_width, s_height))
    screen.blit(bg, (0, 0)) # redraws background image'''


    # Here the action could take place
    # Spielfeld und feste Elemente zeichnen
    pygame.draw.polygon(screen, GREEN, polygon_unten)
    pygame.draw.lines(screen, GREEN, False, outerline_coords, 10)
    #pygame.draw.polygon(screen, RED, fuer_den_anfang_reicht_schraege)
    Polygon.draw(first_collision_trinangle)
    Triangle.draw(power_triangle_left)
    Triangle.draw(power_triangle_right)
    Polygon.draw(gate)
    Circle.draw(circle1)

    
    # list of all polgons and circles
    all_polygons = [first_collision_trinangle, gate]
    all_circles = [circle1]

    # draw ball in startposition
    if gameball.x == ball_startposition_x and gameball.y == ball_startposition_y:
        Ball.draw(gameball)
           
    if ball_release: 
        #Ball.check_closer_sp(gameball, circle1)
        #print(Ball.check_closer_sp(gameball, circle1))
        Ball.update(gameball) 

        # collision with testcircle1
        #Ball.collision_circle(gameball, circle1) 
       
       
    # Rotation arround Point
    


    # Collision with object

    pygame.display.flip() # Update the display of the full screen
    clock.tick(60) # 60 frames per second

# Done! Time to quit.
