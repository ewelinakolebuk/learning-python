from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

#     Detect collision wit wall
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()

#         Detect collision with r_padle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:        ball.bounce_x()

    #     Detect if r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

#     Detect if l_paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()