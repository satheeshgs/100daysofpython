COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        chance_to_create = random.randint(1,6) #ensuring too many cars are not created using random chance
        if chance_to_create == 6:
            car = Turtle("square")        
            car.shapesize(stretch_wid=1,stretch_len=2)
            random_x = 300
            random_y = random.randint(-250,250)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(random_x, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT