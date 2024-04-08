from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ypos = [-80, -50, -20, 10, 40, 70]

#set turtles to race
for i in range(len(colors)):
    jfk = Turtle(shape="turtle")
    jfk.color(colors[i])
    jfk.up()
    jfk.goto(-230,ypos[i])

screen.exitonclick()