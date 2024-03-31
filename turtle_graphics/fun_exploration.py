#Turtle graphics
from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
timmy.shape("triangle")
timmy.color("PeachPuff")
timmy.pencolor("DarkOrchid")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()

table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Psyduck", "Psychic"])
table.align = 'l'
print(table)