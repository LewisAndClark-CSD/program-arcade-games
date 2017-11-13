import pygame
import turtle 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Initialize the game engine
pygame.init()
 

 
PI = 3.141592653


screen = turtle.Screen() 
screen.setup(800,600)






triangle=turtle.Turtle() 
triangle.shape('triangle')
triangle.speed('fastest') 
triangle.color('yellow') 
triangle.up() 
triangle.goto(0,275) 
triangle.stamp() 


square = turtle.Turtle() 
square.shape('square') 
square.color('green') 
square.speed('fastest') 


k = 0 # input
for a in range(1, 8): 
    y = 30 * a 
    for b in range(a - k): 
        x = 30 * b
        square.goto(x, -y + 280) 
        square.stamp() 
        square.goto(-x, -y + 280) 
        square.stamp() 


circle = turtle.Turtle() 
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color('blue')
circle.goto(180, 100)
circle.stamp()
circle = turtle.Turtle()
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color('blue')
circle.goto(-180, 100)
circle.stamp()
circle = turtle.Turtle()
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color('orange')
circle.goto(120, 160)
circle = turtle.Turtle()
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color('orange')
circle.goto(-120, 160)
circle.stamp()
circle.stamp()
circle = turtle.Turtle()
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color("red")
circle.goto(60, 220)
circle.stamp()
circle = turtle.Turtle()
circle.shape('circle')
circle.speed('fastest')
circle.up()
circle.color("red")
circle.goto(-60, 220)
circle.stamp()
square.color('brown') 
for a in range(2,4): 
    y = 30 * a 
    for b in range (2): 
        x = 30 * b 
        square.goto(x, -y + 100) 
        square.stamp() 
        square.goto(-x, -y + 100) 
        square.stamp() 


turtle.exitonclick() 

pygame.quit()