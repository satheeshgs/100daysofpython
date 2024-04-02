from turtle import Turtle, Screen
import random

scene = Screen()
scene.colormode(255)

jfk = Turtle()
jfk.pensize(15)
jfk.speed("fastest") #use 0 for numerical for fastest

directions = [0, 90, 180, 270]

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)


for i in range(0,100):
    jfk.pencolor(random_color()) #choosing a random pen color
    jfk.forward(25)
    direction = random.choice(directions)
    jfk.setheading(direction)






scene.exitonclick()