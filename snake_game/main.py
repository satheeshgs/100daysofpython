from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    #moving the snake forward by moving the last segment to move forward to the previous segment 
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    #detect collision with sides
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #is_game_on = False
        scoreboard.reset()
        snake.reset()


    #detect collision with tail
    for segment in snake.segments[1:]: #all segments except the head
        if snake.head.distance(segment) < 10:
            #is_game_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()