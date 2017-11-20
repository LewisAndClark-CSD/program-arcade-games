#!/usr/bin/env python3
# part_4.py
# Ryan Moore
# 11/15/2017

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE= (0, 0, 255)
PI = 3.141592653
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False 
clock = pygame.time.Clock()
 
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
    # background image.
    screen.fill(BLUE)
 
    # --- Go ahead and update the screen with what we've drawn.
    for y in range(0, 500, 8):
        for x in range(0, 700, 8):
            pygame.draw.rect(screen,RED,[x, y, 4, 4],0)
        print()
                    
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()