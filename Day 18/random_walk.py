import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(10)
turtle.colormode(255)
tim.speed(0)

def color():
    r = random.randrange(0,256,10)
    g = random.randrange(0,256,10)
    b = random.randrange(0,256,10)
    return r, g, b
def random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)
while True:

    tim.pencolor(color())
    tim.setheading(random_direction())
    tim.forward(20)

screen = Screen()
screen.exitonclick()