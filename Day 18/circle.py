import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(1)
turtle.colormode(255)
tim.speed(0)

def color():
    r = random.randrange(0,256,10)
    g = random.randrange(0,256,10)
    b = random.randrange(0,256,10)
    return r, g, b
for _ in range(120): #360/tim.right(3)
    tim.right(3)
    tim.pencolor(color())
    tim.circle(90)

screen = Screen()
screen.exitonclick()