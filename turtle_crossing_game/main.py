import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    carmanager.create_car()
    carmanager.move_cars()

    #increase level based on turtle crossing successfully
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        carmanager.increase_speed()
    
    #detect collisions with cars
    for car in carmanager.all_cars:
        if player.distance(car) < 20: 
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()