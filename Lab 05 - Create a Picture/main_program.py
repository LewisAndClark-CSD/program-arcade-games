#!/usr/bin/env python3
#Lab #5
#Christian Groves
#11/16/17
import pygame
pygame.init()
BLACK   =(0,0,0)
WHITE   =(255,255,255)
GREEN   =(0,255,0)
RED     =(255,0,0)
BLUE    =(0,0,255)
size=(700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Christian's Cool Game")
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
            
    screen.fill(BLUE)        
    
    pygame.draw.line(screen, GREEN , [0,400], [700,400],200)        
    pygame.draw.ellipse(screen, WHITE, [20, 20, 250, 100], 50)
    
    
         
    pygame.display.flip()        
             
    clock.tick(20)
    
pygame.quit  ()