from turtle import Turtle, Screen
import random

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)

jfk = Turtle()
jfk.speed("fastest")
scene = Screen()
scene.colormode(255)

#spirograph
for i in range(120):
    jfk.pencolor(random_color())
    jfk.circle(100)
    jfk.setheading(i*3)



scene.exitonclick()