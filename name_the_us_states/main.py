import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.to_list()

game_is_on = True

while game_is_on:
    user_guess = screen.textinput(title="Guess the states", prompt="What's the state name that you are guessing?")
    user_guess = user_guess.title()
    if user_guess in all_states:
        user_guess_x = states_data.loc[states_data.state == user_guess, 'x'].iloc[0]  #find user guess x value
        user_guess_y = states_data.loc[states_data.state == user_guess, 'y'].iloc[0]  #find user guess y value
        state_turtle = turtle.Turtle() #create a new turtle on the screen to move to user location
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(user_guess_x, user_guess_y)
        state_turtle.write(user_guess)  #display user guess in (x,y) location

turtle.mainloop()
