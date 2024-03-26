#number guessing
from art import logo
from clear import clearscreen
import random
import time
game_mode = {'h': 5, 'e': 10}

to_continue = 'y'
while to_continue == 'y':
    print(logo)
    time.sleep(1)
    choice = input("Which mode do you want to play? Enter 'h' for hard mode (5 guesses) or 'e' for easy mode (10 guesses): ")
    number_of_guesses = game_mode[choice]
    computer_guess = random.randint(1,100)
    
    game_over =  False
    while game_over == False:
        print(f"You have {number_of_guesses} left.")
        user_guess = input("Guess your number: ")
        
        to_continue = 'n'