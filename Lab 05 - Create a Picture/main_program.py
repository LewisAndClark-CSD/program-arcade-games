#!/usr/bin/env python3
#Lab 5 Draw a Picture
#Bethany DuMontelle
#8 November 2017

#Starts up pygame
import pygame
pygame.init()

#Establishes colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (74, 224, 129)

size = (800, 800)
screen = pygame.display.set_mode(size)

done = False
while not done:
    
    pygame.draw.ellipse(screen, LIGHT_GREEN, [50, 50, 40, 40], 5)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
pygame.quit()