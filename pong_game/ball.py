from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(-45)
    
    def move(self):
        self.forward(10)
    
    def bounce(self):
        if self.ycor() > 250:
            self.setheading(self.heading() - 90)
        else:
            self.setheading(self.heading() + 90)

