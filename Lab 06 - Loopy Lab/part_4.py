#!/usr/bin/env python3
#part_4.py
#Ethan Dall
#11-15-17

"""Drawing a screen full of small rectangles"""

#import

import pygame

#initialize

pygame.init()

#Define Colors

ORANGE = (247, 152, 36)
BLACK = (0, 0, 0)

#Window

size = (700, 500)
screen = pygame.display.set_mode(size)

#Name

pygame.display.set_caption('Orange Infinity')

#Condition

done = False

#Clock

clock = pygame.time.Clock()

#Program initializer

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Background
    
    screen.fill(BLACK)
    
    #Rectangles
    
    for y in range(0, 700, 15):
        for x in range(0, 700, 10):
            sqr = pygame.draw.rect(screen, ORANGE, [(x,y), (5,5)], 0)
                
    
    #End
    
    pygame.display.flip()
    clock.tick(30)
    
#IDLE friendly
pygame.quit()