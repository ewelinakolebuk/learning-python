import turtle
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(1)
# turtle.colormode(255)
tim.speed(0)

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()