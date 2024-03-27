#number guessing
from art import logo
from clear import clearscreen
import random
import time
game_mode = {'h': 5, 'e': 10}

def guess_check(num1, num2):
    if num1 > num2:
        return "Too High"
    elif num1 < num2:
        return "Too Low"
    else:
        return "Correct"

to_continue = 'y'
while to_continue == 'y':
    clearscreen()
    print(logo)
    time.sleep(1)
    choice = input("Which mode do you want to play? Enter 'h' for hard mode (5 guesses) or 'e' for easy mode (10 guesses): ")
    number_of_guesses = game_mode[choice]
    computer_guess = random.randint(1,100)
    
    game_over =  False
    while game_over == False:
        print(f"You have {number_of_guesses} guesses left.")
        user_guess = int(input("Guess your number: "))

        while guess_check(user_guess, computer_guess) != "Correct":
            print(guess_check(user_guess, computer_guess))
            number_of_guesses -= 1
            print(f"You have {number_of_guesses} guesses left.")
            user_guess = int(input("Guess your number: "))
        
        if guess_check(user_guess, computer_guess) == "Correct":
            print(f"Congratulations. You guessed correctly. The number is {user_guess}")
            break
        else:
            print("You ran out of guesses. You lose")
            break

    to_continue = input("Do you want to start a new game? Type 'y' for yes and 'n' for no: ")