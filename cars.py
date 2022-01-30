from turtle import Turtle
import random
Y_POS=[-217.35,-192.05,-166.75,-141.45,-116.15,-90.85,-65.55,-40.25,-14.95,10.35,35.65,60.95,86.25,111.55,136.85,162.15,187.45,212.75,238.05]
COLOR=["green","yellow","pink","black","white","blue","cyan","pale goldenrod","green yellow","indigo","medium violet red","purple"]
class Car (Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.8,stretch_len=2)
        self.goto(x,random.choice(Y_POS))
        self.color(random.choice(COLOR))

    def move(self):
        self.goto(self.xcor()-random.randint(1,10),self.ycor())