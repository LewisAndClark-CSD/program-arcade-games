#!/usr/bin/env python3
# main_program.py
# Jared Rhodes
# 11/09/2017

""" This is the draw pictue lab from chapter 5 """

import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKYBLUE = (0, 255, 255)
BROWN = (155, 100, 0)
BLUE = (0, 0, 255)
PI = 3.1415926

pygame.init()
size = (700, 500)
max_X = 700
max_Y = 500
screen = pygame.display.set_mode(size)

done = False


clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GREEN, [0, 400, 700, 500])
    pygame.draw.ellipse(screen, BLUE, [100,340,220,120])
    pygame.draw.rect(screen, SKYBLUE, [0, 0, 700, 400])
    pygame.draw.circle(screen, YELLOW, [100, 100], 100)
    pygame.draw.rect(screen, BROWN, [400, 350, 30, 80])
    pygame.draw.circle(screen, GREEN, [415, 250], 100)
    pygame.draw.lines(screen, BLACK, False, [(600, 100), (610, 110), (620, 100)], 4)
    pygame.draw.lines(screen, BLACK, False, [(500, 140), (510, 150), (520, 140)], 3)
    pygame.draw.lines(screen, BLACK, False, [(550, 180), (560, 190), (570, 180)], 2)
    pygame.draw.circle(screen, RED, [360, 220], 9)
    pygame.draw.circle(screen, RED, [430, 240], 9)
    pygame.draw.circle(screen, RED, [460, 200], 9)
    pygame.draw.circle(screen, RED, [420, 320], 9)
    pygame.draw.circle(screen, RED, [350, 295], 9)
    pygame.draw.circle(screen, RED, [480, 285], 9)
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()