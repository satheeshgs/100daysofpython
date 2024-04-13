from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

jfk = Snake()

screen.listen()
screen.onkey(jfk.up, "Up")
screen.onkey(jfk.down, "Down")
screen.onkey(jfk.left, "Left")
screen.onkey(jfk.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    #moving the snake forward by moving the last segment to move forward to the previous segment 
    jfk.move()




screen.exitonclick()