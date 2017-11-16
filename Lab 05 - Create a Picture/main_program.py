#!/usr/bin/env python3
#main_program.py
#Justin Riebow
#11/7/17

"""A pretty picture"""

import pygame

yellow = (235, 244, 66)
lightBlue = (66, 131, 244)
green = (0, 142, 60)
brown = (49, 53, 0)
black = (0, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rainy Day")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(lightBlue)
    pygame.draw.rect(screen, green, [0, 400, 700, 100 ])
    pygame.draw.rect(screen, brown, [250, 200, 200, 200])
    pygame.draw.polygon(screen, brown, [[350, 100],[250, 200], [450, 200]])
    pygame.draw.rect(screen, black, [325, 325, 50, 75])
    pygame.draw.ellipse(screen, yellow, [20, 20, 100, 100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
