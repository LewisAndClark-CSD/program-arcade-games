#!/usr/bin/env python 3
#Destroy The City PyGame
 >>>>>>> d65a200f26d213f86446b9aa3fa7733773ae286a
 
 import pygame
 
 WHITE = (255, 255, 255)
 GREEN = (144, 212, 178)
 PINK = (209, 21, 184)
 BLUE = (75, 51, 232)
 YELLOW = (226, 232, 51)
 BLACK = (0, 0, 0)
 BROWN = (87, 59, 23)
 PI = 3.141592653
 
 pygame.init()
  
 # Set the width and height of the screen [width, height]
 size = (700, 500)
 screen = pygame.display.set_mode(size)
 pygame.display.set_caption("Destroy The City")
  
 # Loop until the user clicks the close button.
 done = False
  
 # Used to manage how fast the screen updates +clock = pygame.time.Clock()
  
 # -------- Main Program Loop -----------
 while not done:
     # --- Main event loop
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
 
     # If you want a background image, replace this clear with blit'ing the
     # background image.
     screen.fill(BLACK)
 
         # Draw a rectangle
     pygame.draw.rect(screen, BLUE, [120, 150, 100, 200])
     pygame.draw.rect(screen, BLUE, [470, 150, 100, 200])
     pygame.draw.rect(screen, GREEN, [580, 150, 100, 200])
     pygame.draw.rect(screen, GREEN, [10, 150, 100, 200])
     # The top row of 'windows' on the buildings
     pygame.draw.rect(screen, YELLOW, [20, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [70, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [130, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [180, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [480, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [530, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [590, 170, 30, 20])
     pygame.draw.rect(screen, YELLOW, [640, 170, 30, 20])
     # The middle row of 'windows' on the buildings
     pygame.draw.rect(screen, YELLOW, [20, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [70, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [130, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [180, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [480, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [530, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [590, 220, 30, 20])
     pygame.draw.rect(screen, YELLOW, [640, 220, 30, 20])
     # The bottom row of 'windows' on the buildings
     pygame.draw.rect(screen, YELLOW, [20, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [70, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [130, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [180, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [480, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [530, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [590, 270, 30, 20])
     pygame.draw.rect(screen, YELLOW, [640, 270, 30, 20])
     # The 'doors' on the buildings'
     pygame.draw.rect(screen, BROWN, [35, 300, 50, 50])
     pygame.draw.rect(screen, BROWN, [145, 300, 50, 50])
     pygame.draw.rect(screen, BROWN, [495, 300, 50, 50])
     pygame.draw.rect(screen, BROWN, [605, 300, 50, 50])
  
     # Draw an arc as part of an ellipse.
     # Use radians to determine what angle to draw.
     pygame.draw.arc(screen, WHITE, [220, 150, 250, 200], 0, PI / 2, 2)
     pygame.draw.arc(screen, GREEN, [220, 150, 250, 200], PI / 2, PI, 2)
     pygame.draw.arc(screen, BLUE, [220, 150, 250, 200], PI, 3 * PI / 2, 2)
     pygame.draw.arc(screen, YELLOW, [220, 150, 250, 200], 3 * PI / 2, 2 * PI, 2)
  
     # Select the font to use, size, bold, italics
     font = pygame.font.SysFont('Calibri', 25, True, False)
  
     # Render the text. "True" means anti-aliased text.
     # White is the color. This creates an image of the
     # letters, but does not put it on the screen
     text = font.render("Button to Destroy All", True, WHITE)
  
     # Put the image of the text on the screen at 245x240
     screen.blit(text, [245, 240])
     
     pygame.display.flip()
  
     # --- Limit to 60 frames per second
     clock.tick(60)
  
 # Close the window and quit.
 <<<<<<< HEAD
 pygame.quit()
 =======
 pygame.quit() 
