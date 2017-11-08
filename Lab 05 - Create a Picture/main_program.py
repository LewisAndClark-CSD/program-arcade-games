#!/usr/bin/env python3
#picture perfect
#Ethan Dall
#11-6-17

"""Drawing a campfire"""

#import

import pygame
from math import pi
import random

#initializing

pygame.init()

#Defining Colors
#Fixed

ORANGE = (221, 61, 27)
RED = (214, 35, 20)
YELLOW = (241, 169, 51)
GREY = (100, 100, 100)
BROWN = (137, 70, 44)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Window

size = (700, 500)
screen = pygame.display.set_mode(size)

#Name

pygame.display.set_caption('Fire in the Night')

#condition

done = False

#Clock

clock = pygame.time.Clock()

#While; Program initalizer sequence

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Sets background
    
    screen.fill(BLACK)

#Stars
    
    for i in range(0, 700):
        x = random.randint(0, 700)
        pygame.draw.ellipse(screen, WHITE, [(x, i), (1, 1)], 0)
    
    #Fire
    
    for i in range(500):
        x = random.randint(200, 250)
        pygame.draw.ellipse(screen, ORANGE, [(x, i), (x, i)], 0)
        pygame.draw.ellipse(screen, YELLOW, [(x, i), (x, i)], 0)
        pygame.draw.ellipse(screen, RED, [(x, i), (x, i)], 0)


    #Ground
    
    pygame.draw.line(screen, BROWN, (0,475), (700, 475), 75)
        
    #Brazen
    
    pygame.draw.rect(screen, GREY, [(200, 500), (300, 500)], 150)
    pygame.draw.circle(screen, WHITE, (50, 50), 50, 0)
    
    #End init
    
    pygame.display.flip()
    clock.tick(30)
    
    

#IDLE friendly
pygame.quit()

#Notes
#Defining Rectangles pygame.draw.rect(Surface, color, cords[4-points], width)
#Defining Lines pygame.draw.line(Surface, color, cord[2-points], cords[2-points], width)
#Use a While loop to add iteration to lines
#Using a for loop to use trig functions
#Defining Ellipse with pygame.draw.ellipse(Surface, color, cords[4-points], width)
#Defining arc with pygame.draw.arc(Surface, color, cords(4-points), [2 radians seperated with a comma])
#Defing polygons with pygame.draw.polygon(Surface, color, cords[[2-points],[2-points],[2-points]], width)
