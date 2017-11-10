#!/usr/bin/env python3
# Drawing a picture in python
# Evan Witterholt
# 11/11/17

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
size = (700, 500)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(GREEN)

    pygame.draw.rect(screen,BLACK,[-25,35,750,150],2)

    pygame.display.flip()

    clock.tick(60)

  
pygame.quit()



