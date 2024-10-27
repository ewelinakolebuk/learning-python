import turtle
import random
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]

turtles = []
for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True
while is_race_on:
    turtle.speed(0)
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
                break
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
                break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()