#Turtle graphics
from turtle import Turtle, Screen
from prettytable import PrettyTable

jfk = Turtle()
jfk.shape("triangle")
jfk.color("PeachPuff")
jfk.pencolor("DarkOrchid")
jfk.forward(100)

table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Psyduck", "Psychic"])
table.align = 'l'
print(table)


def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

jfk.shape('triangle')
jfk.color('DarkSalmon')
jfk.pencolor('Maroon')

for i in range(5):
    jfk.down()
    jfk.forward(10)
    jfk.up()
    jfk.forward(10)

#draw_square(jfk)

#different shapes
jfk.down()

def draw_shapes(sides):

    for _ in range(sides):
        angle = 360/ sides
        jfk.forward(20)
        jfk.right(angle)

for i in range(3,11):
    draw_shapes(i)


my_screen = Screen()
my_screen.exitonclick()