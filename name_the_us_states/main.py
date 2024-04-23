import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")

game_is_on = True

while game_is_on:
    user_guess = screen.textinput(title="Guess the states", prompt="What's the state name that you are guessing?")
    user_guess = user_guess.title()
    user_guess_x = states_data.loc[states_data.state == user_guess, 'x'].iloc[0]  #find user guess x value
    user_guess_y = states_data.loc[states_data.state == user_guess, 'y'].iloc[0]  #find user guess y value
    turtle.setposition(user_guess_x, user_guess_y)
    turtle.write(user_guess)  #display user guess in (x,y) location

turtle.mainloop()
