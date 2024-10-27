# #####Turtle Intro######
#
# import turtle as t
#
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)
import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(3)

# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)
def color():
    r = random.randrange(0,256,10)
    g = random.randrange(0,256,10)
    b = random.randrange(0,256,10)
    return r, g, b


figure = 3
while True:
    turtle.colormode(255)
    new_color = color()
    tim.pencolor(new_color)
    for _ in range(figure):
        tim.forward(120)
        tim.right(360/figure)
    figure += 1
    if figure == 11:
        break

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

screen = Screen()
screen.exitonclick()



