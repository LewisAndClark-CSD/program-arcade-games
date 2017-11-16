#!/usr/bin/env python3
# Lab 03 Creat a Picture
# Conner Walkenhorst
# 11/10/2017

"""Create a picture from python code"""

import pygame

# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Conner's Python House")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(BLACK)
 
    # Draw a rectangle for grass
    pygame.draw.rect(screen, GREEN, [0, 400, 500, 100], 0)
    
    # Draw a rectangle for house
    pygame.draw.rect(screen, BLUE, [150, 200, 200, 200], 0)
    
    #draw a rectangle for door
    pygame.draw.rect(screen, RED, [200, 400, 100, -95], 0)
    
    #draw an ellipse for door knob
    pygame.draw.ellipse(screen, BLACK, [265, 335, 15, 15], 0)
 
    # This draws a triangle for the house using the polygon command
    pygame.draw.polygon(screen, RED, [[250, 75], [150, 200], [350, 200]], 0)
 
 # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLUE, [200, 130, 100, 50], 0)
    
    #draw an ellipse for the moon
    pygame.draw.ellipse(screen, WHITE, [60, 60, 60, 60], 0)
    
    #draw a line for upper window
    pygame.draw.line(screen, BLACK, [250, 130], [250, 177], 2)
    
    #draw other line for upper window
    pygame.draw.line(screen, BLACK, [200, 150], [300, 150], 2)
    
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text = font.render("Hello World", True, BLACK)
 
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [200, 250])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
