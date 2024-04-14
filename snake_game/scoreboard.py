from turtle import Turtle
FONT = "Arial"
ALIGNMENT = "center"
SCOREBOARD_POSITION = (-50,280)

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

    def increase_score(self):
        self.score += 1
        self.print_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=(FONT, 16, 'normal'))
        