#!/usr/bin/env python3
#Picture game
#Ryan Rosvall
#11/3/17

import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

size=[700,500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ryan's Super Cool Drawing Game")

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(white)

    pygame.draw.rect(screen, black, [150, 150, 350, 300])

    #for x in range(0, 100, 20):
    for x in range(150, 350, 50):
        pygame.draw.line(screen, black, [150, 150], [350, 100], 5)
        pygame.draw.line(screen, black, [150, 158], [350, 108], 2)
        pygame.draw.line(screen, black, [150, 166], [350, 116], 2)
        pygame.draw.line(screen, black, [150, 174], [350, 124], 2)
    pygame.draw.line(screen, black, [350, 150], [350, 100], 5) #downline

    font = pygame.font.Font(None, 20)

    text = font.render('Pg.9', True, black)
    screen.blit(text, [315,135] )


    pygame.draw.ellipse(screen, green, [350, 350, 40, 40])
    pygame.draw.ellipse(screen, green, [250, 350, 40, 40])
    pygame.draw.rect(screen, white, [250, 250, 140, 100])
    pygame.draw.rect(screen, white, [380, 300, 50, 50])

    #pygame.draw.rect(screen, black, [50, 50, 250, 100]
    
    pygame.display.flip()


    clock.tick(20)

pygame.quit()

