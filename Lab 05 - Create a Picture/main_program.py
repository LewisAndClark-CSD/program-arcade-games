# !/usr/bin/env python3
# picture
# Ryan Moore
# 11/09/2017

import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PI = 3.141592653
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False 
clock = pygame.time.Clock()
 
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
 
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,[250,250,250,250],2)
    pygame.draw.line(screen,BLACK, [300, 300], [350, 300], 2)    
    pygame.draw.line(screen,BLACK, [300, 300], [300, 350], 2)    
    pygame.draw.line(screen,BLACK, [350, 300], [350, 350], 2)    
    pygame.draw.line(screen,BLACK, [300, 350], [350, 350], 2)    
    pygame.draw.circle(screen,YELLOW, (625, 75), 50, 0)
    pygame.draw.line(screen,BLACK, [350, 450], [400, 450], 2)    
    pygame.draw.line(screen,BLACK, [350, 450], [350, 500], 2)    
    pygame.draw.line(screen,BLACK, [400, 450], [400, 500], 2)    
    pygame.draw.polygon(screen, BLACK, [[500,250], [250,250], [375,150]], 2)
     
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
