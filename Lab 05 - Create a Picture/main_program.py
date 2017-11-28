#!/usr/bin/env python3
#Lab 5 Draw a Picture
#Bethany DuMontelle
#8 November 2017

#Starts up pygame
import pygame
pygame.init()

#Establishes colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (74, 224, 129)
LIGHT_BLUE = (52, 198, 247)
DEEP_PURPLE = (79,18,201)
SKY = (235, 193, 96)
SUN_YELLOW = (246, 255, 0)
SUN_RING = (219, 222, 95)
PANK = (235, 103, 226)
RED = (224, 13, 52)

size = (800, 800)
screen = pygame.display.set_mode(size)

done = False
while not done:
    
    #changes background color
    screen.fill(SKY)
    
    #Makes the ocean
    pygame.draw.rect(screen, LIGHT_BLUE, [0, 350, 800, 800], 0)
    
    #Creates ring around the sun
    pygame.draw.circle(screen, SUN_RING, [10, 10], 140, 0)
    
    #Creates the sun
    pygame.draw.circle(screen, SUN_YELLOW, [10, 10], 100, 0)
    
    #octopus legs
    pygame.draw.line(screen, DEEP_PURPLE, [300, 350], [125, 500], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [300, 380], [220, 600], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [340, 380], [300, 620], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [380, 380], [360, 590], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [420, 380], [420, 625], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [460, 380], [480, 595], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [500, 380], [550, 585], 40)
    pygame.draw.line(screen, DEEP_PURPLE, [510, 350], [630, 570], 40)
    
    #octopus body
    pygame.draw.ellipse(screen, DEEP_PURPLE, [275, 200, 250, 275], 0)
    
    #octopus eyes
    pygame.draw.ellipse(screen, WHITE, [335, 300, 35, 35], 0)
    pygame.draw.ellipse(screen, BLACK, [340, 310 , 25, 25], 0)
    pygame.draw.ellipse(screen, WHITE, [435, 300, 35, 35], 0)
    pygame.draw.ellipse(screen, BLACK, [440, 310 , 25, 25], 0)
    
    #octopus mouth
    pygame.draw.polygon(screen, PANK, [[400, 420], [440, 360], [360, 360]], 0)
    pygame.draw.polygon(screen, RED, [[400, 412], [420, 380], [380, 380]], 0)
    
    #Seaweed
    x_offset = 20
    while x_offset < 780:
        pygame.draw.line(screen, LIGHT_GREEN, [20 + x_offset, 600],\
        [20 + x_offset, 800], 15) 
        x_offset = x_offset + 40
    
    #updates the screen to show the picture
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
pygame.quit()