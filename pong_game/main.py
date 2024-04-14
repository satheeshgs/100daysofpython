from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

STARTING_POSITIONS = [(350,0), (-350,0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


#creating and moving the paddle
r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()












screen.exitonclick()