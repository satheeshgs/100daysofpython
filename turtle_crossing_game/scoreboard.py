FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-260,260)
ALIGNMENT = "left"

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 1
        self.initial_setup()
        self.print_score()
        
    def initial_setup(self):
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.pencolor("black")
    
    def print_score(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
        