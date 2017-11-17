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
PURPLE  =(150,20,130)
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
    #green ground
    pygame.draw.line(screen, GREEN , [0,400], [700,400],200) 
    #first cloud
    pygame.draw.ellipse(screen, WHITE, [40, 20, 130, 90])
    pygame.draw.ellipse(screen, WHITE, [70, 30, 140, 110])
    pygame.draw.ellipse(screen, WHITE, [20, 40, 140, 110])
    #second cloud
    pygame.draw.ellipse(screen, WHITE, [440, 50, 140, 110])
    pygame.draw.ellipse(screen, WHITE, [460, 20, 140, 110])
    pygame.draw.ellipse(screen, WHITE, [480, 60, 140, 110])
    #House
    pygame.draw.rect(screen, PURPLE, [300, 320, 300, 320])
    
    
    
    
    
         
    pygame.display.flip()        
             
    clock.tick(20)
    
pygame.quit  ()