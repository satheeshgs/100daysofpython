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
def spirograph(turn_angle):

    for i in range(int(360/turn_angle)):
        jfk.pencolor(random_color())
        jfk.circle(100)
        jfk.setheading(i*turn_angle)


spirograph(5)

scene.exitonclick()