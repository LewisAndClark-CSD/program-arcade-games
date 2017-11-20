#!/usr/bin/env python3
#part_4.py
#Justin Riebow
#11/16/17
"""Create an image using small rectangles"""

import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            
    screen.fill(BLACK)
    
    for y in range(0, 500, 20):
        for x in range(0, 500, 20):
            pygame.draw.rect(screen, BLUE, (x, y, 10, 10))
    
    pygame.display.flip()
    
    
    clock.tick(60)
    
pygame.quit()



