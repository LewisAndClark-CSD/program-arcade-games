#!/usr/bin/env python3
# main_program for chapter 5 lab
# Brady Ballmann
# 11/09/2017


import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKY =  (135, 206, 250)
BROWN = (139,69,19)
WHEAT = (245,222,179)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY)
    
     # These are Lines and they are the tree
    pygame.draw.line(screen, BROWN, [10, 600], [10, 400], 10)

    pygame.draw.line(screen, BROWN, [85, 600], [85, 400], 10)
    
    pygame.draw.line(screen, BROWN, [160, 600], [160, 400], 10)

    pygame.draw.line(screen, WHEAT, [300, 470], [300, 400], 5)

    pygame.draw.line(screen, WHEAT, [300, 470], [270, 600], 5)

    pygame.draw.line(screen, WHEAT, [300, 470], [350, 600], 5)

    pygame.draw.line(screen, WHEAT, [275, 440], [325, 440], 5)

    pygame.draw.line(screen, BROWN, [690, 600], [690, 400], 10)

    pygame.draw.line(screen, BROWN, [625, 600], [625, 400], 10)

    pygame.draw.line(screen, BROWN, [550, 600], [550, 400], 10)

    pygame.draw.line(screen, BLACK, [375, 600], [375, 475], 7)

    pygame.draw.line(screen, BLACK, [450, 600], [450, 475], 7)

    pygame.draw.line(screen, BLACK, [375, 475], [450, 475], 5)

    


    # Circles

    pygame.draw.circle(screen, GREEN, (20,350), 65,0)

    pygame.draw.circle(screen, GREEN, (90,350), 65,0)

    pygame.draw.circle(screen, GREEN, (160,350), 65,0)

    pygame.draw.circle(screen, WHEAT, (300,400), 20,0)

    pygame.draw.circle(screen, WHITE, (295,395), 3,0)

    pygame.draw.circle(screen, WHITE, (305,395), 3,0)

    pygame.draw.circle(screen, GREEN, (690,350), 65,0)

    pygame.draw.circle(screen, GREEN, (620,350), 65,0)

    pygame.draw.circle(screen, GREEN, (550,350), 65,0)

    pygame.draw.circle(screen, YELLOW, (20,20), 80,0)
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

