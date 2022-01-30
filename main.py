import random
from turtle import Screen,Turtle
from cars import Car
import time
from scoreboard import Scoreboard
import random
screen= Screen()
screen.bgcolor("lightgrey")
screen.setup(width=600,height=600)
screen.tracer(0)
player =Turtle()
player.penup()
player.shape("turtle")
player.setheading(90)
player.color("green")
screen.title("Made By: Raz Dvora")
player.goto(x=0,y=-280)
player_is_alive = True
lvl =1
screen.listen()
scoreboard = Scoreboard()
lane=Turtle()
lane.penup()
y_lane=-230
lane.hideturtle()
lane.pensize(3)
for lanes in range (20):
    lane.goto(x=-300, y=y_lane)
    lane.pencolor("white")
    lane.pendown()
    while lane.xcor()<300:
            lane.forward(random.randint(1,10))
            lane.pendown()
            lane.forward(random.randint(2,10))
            lane.penup()

    y_lane+=25.3
    lane.penup()

def player_move():
    player.goto(0,player.ycor()+10)

screen.onkey(player_move,"Up")
cars=[]
for new_car in range(500):
    new_car=Car(random.randint(300,15000))
    cars.append(new_car)


while player_is_alive:
    time.sleep(0.1/lvl)
    screen.update()

    for car in cars:
        car.move()
        if player.distance(car) < 20:
            screen.title("GAME OVER")
            player_is_alive=False
            scoreboard.game_over()
    if player.ycor()>266:
        player.goto(0,-260)
        scoreboard.score+=1
        scoreboard.update_score()
        lvl+=1
screen.exitonclick()