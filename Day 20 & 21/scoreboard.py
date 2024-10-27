from turtle import Turtle
ALIGN = "center"
FONT =("Courier", 16, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)
