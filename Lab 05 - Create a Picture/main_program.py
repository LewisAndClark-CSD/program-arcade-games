#!/usr/bin/env python3
#Lab #5
#Christian Groves
#11/16/17
import pygame
pygame.init()
greenColor = 175
radius = 180
sunChange= (200,greenColor,40)
LIGHTBLUE=(126,213,242)
BLACK   =(0,0,0)
WHITE   =(255,255,255)
GREEN   =(0,255,0)
RED     =(255,0,0)
BLUE    =(0,0,255)
PURPLE  =(150,20,130)
size=(700,500)
xoff= 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Christian's Cool Game")
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
while done == False:
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    #House's
    for xoff in range(700, 0, -200):
        pygame.draw.rect(screen, PURPLE, [50+ xoff , 260, 100, 110])
        pygame.draw.rect(screen, BLACK, [70+ xoff , 300, 30, 70])
        pygame.draw.rect(screen, WHITE, [110+ xoff , 300, 30, 30])
        pygame.draw.polygon(screen, RED, [[25+ xoff , 260], [175+ xoff, 260], [100+ xoff , 200]]) 
    
         
    pygame.display.flip()        
             
    clock.tick(20)
    
pygame.quit  ()