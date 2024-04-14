from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.setheading(45)
    
    def move(self):
        self.forward(20)
        time.sleep(0.05)
