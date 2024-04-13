from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ypos = [-80, -50, -20, 10, 40, 70]

#set turtles to race
turtles = []
for i in range(len(colors)):
    jfk = Turtle(shape="turtle")
    jfk.color(colors[i])
    jfk.up()
    jfk.goto(-230,ypos[i])
    turtles.append(jfk)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You guessed right. The {winning_turtle} turtle won")
            else:
                print(f"You guessed wrong. The winning turtle's color is {winning_turtle}")
        
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)

screen.exitonclick()