import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle=Player()
car_manager=CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_new_car()
    car_manager.move()

    #Detect collision with car:
    for car in car_manager.all_cars:
        if turtle.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
    if turtle.ycor() > 280:
        scoreboard.update_scoreboard()
        turtle.return_tu_start_position()
        car_manager.level_up()
screen.exitonclick()