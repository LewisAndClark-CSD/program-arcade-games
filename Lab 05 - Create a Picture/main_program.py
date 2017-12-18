#
import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
tan = (244, 204, 159)
PI = 3.141592653

size=[700,500]
screen=pygame.display.set_mode(size)


pygame.display.set_caption('Cole"s cool drawing game')

done = False

clock=pygame.time.Clock()

while done ==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True


    
    screen.fill(white)

    
    pygame.draw.line(screen, tan, [350, 300], [350, 200], 5)
    pygame.draw.line(screen, tan, [350,250 ], [275, 220], 5)
    pygame.draw.line(screen, tan, [350,250 ], [420, 220], 5)
    pygame.draw.line(screen, tan, [350,300 ], [275, 375], 5)
    pygame.draw.line(screen, tan, [350,300 ], [420, 375], 5)
    pygame.draw.ellipse(screen, tan, [275, 50, 150, 150], 3)
    pygame.draw.ellipse(screen, tan, [315, 160, 70, 20], 3)
    pygame.draw.ellipse(screen, tan, [305, 110, 30, 15], 3)
    pygame.draw.ellipse(screen, tan, [360, 110, 30, 15], 3)
    pygame.display.flip()
    clock.tick(20)
    
