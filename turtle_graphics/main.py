#hirst painting
from turtle import Turtle, Screen

jfk = Turtle()
jfk.shape('triangle')
jfk.color('DarkSalmon')
jfk.pencolor('Maroon')

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

for i in range(5):
    jfk.down()
    jfk.forward(10)
    jfk.up()
    jfk.forward(10)

#draw_square(jfk)














my_screen = Screen()
my_screen.exitonclick()