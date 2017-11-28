#!/usr/bin/env python3
#Lab Part 4
#Bethany DuMontelle
#17 November 2017

#start pygame
import pygame
pygame.init()

#Set up and open up the screen
size = (800, 800)
screen = pygame.display.set_mode(size)

#set the colors for the pattern
LIGHT_BLUE = (52, 198, 247)

#starts the exit option
done = False
while not done:
    
#loop it across the screen
    y_offset = -4
    for x in range(1, 100):
        y_offset = y_offset + 10
        x_offset = 6
        for y in range(1, 100):
            pygame.draw.circle(screen, LIGHT_BLUE, [x_offset, y_offset], 3, 0)
            x_offset = x_offset + 10

#screen updates
    pygame.display.update()
    
#exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
pygame.quit()