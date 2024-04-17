from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.initial_setup()
        self.print_score()

    def initial_setup(self):
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.pencolor("white")
    

    def print_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}", False, align=ALIGNMENT, font=(FONT, 14, 'normal'))