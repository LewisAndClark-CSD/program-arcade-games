#Turtle Tim
import turtle

def draw_diamond(some_turtle):
    some_turtle.left(30)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(120)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(150)

def draw_art():        
    # Instantiate a Screen object, window. Then customize window.
    window = turtle.Screen()
    window.bgcolor("red")     # set background color
    # Instantiate a Turtle object, tim. Then customize tim.
    tim = turtle.Turtle()
    tim.shape("turtle")      # see Turtle doc
    tim.color("white")      # see Turtle doc
    tim.speed(2)             # 1 (slowest) to 10 (fastest). 0 means no animation.

    # Draw a circle with 36 diamonds. We rotate each diamond by 10 degrees at a time.
    for i in range (0, 75):      
        draw_diamond(tim)
        tim.right(5)

    # Draw a between middle of circle and the floor
    tim.right(45)
    tim.forward(200)
    
    # How to exit?
    window.exitonclick()      # click on the window to exit


# Invoke the procedure!
draw_art()
