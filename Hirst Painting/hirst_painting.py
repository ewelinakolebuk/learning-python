# import colorgram
# colors = colorgram.extract("image.jpg", 20)
#
# color_palette = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_palette.append(new_color)
# print(color_palette)
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

color_list = [(183, 178, 2), (193, 153, 84), (169, 2, 73), (250, 73, 1), (251, 15, 154), (3, 140, 7), (37, 197, 240),
              (2, 132, 210), (90, 1, 97), (3, 168, 129), (181, 2, 0), (247, 4, 136), (252, 64, 6), (253, 230, 0),
              (246, 227, 40), (254, 5, 3)]

screen = Screen()
screen.setworldcoordinates(-250, -250, screen.window_width() - 1, screen.window_height() - 1)
tim.penup()
tim.hideturtle()
tim.speed(0)
for _ in range (10):
    for _ in range (10):
        dot_color = random.choice(color_list)
        tim.dot(20, dot_color)
        tim.forward(50)
    y = tim.position()[1]
    tim.goto(0, y+50)

screen.exitonclick()

