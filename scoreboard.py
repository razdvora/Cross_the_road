from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-200,y=250)
        self.write("LVL:"+str(self.score), align="center",font=("Arial",30,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",40,"normal"))