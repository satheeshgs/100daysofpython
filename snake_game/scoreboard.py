from turtle import Turtle
FONT = "Arial"
ALIGNMENT = "center"
SCOREBOARD_POSITION = (-50,280)

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.initial_setup()
        self.print_score()
        
    def initial_setup(self):
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.pencolor("white")

    def get_high_score(self):
        with open("high_score.txt") as file:
            high_score = file.read()
        return high_score

    def set_high_score(self, score):
        with open("high_score.txt", mode='w') as file:
            file.write(f"{score}")    

    def print_score(self):
        self.clear()
        self.high_score = self.get_high_score()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=(FONT, 14, 'normal'))

    def increase_score(self):
        self.score += 1
        self.print_score()
    
    #def game_over(self):
    #    self.goto(0,0)
    #    self.write(f"GAME OVER", False, align=ALIGNMENT, font=(FONT, 16, 'normal'))
        
    def reset(self):
        if self.score > int(self.high_score):
            self.set_high_score(self.score)
        self.score = 0
        self.print_score()