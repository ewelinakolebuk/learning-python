FONT = ("Courier", 18, "bold")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level +=1
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
