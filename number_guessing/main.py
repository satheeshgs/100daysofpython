#number guessing
from art import logo
from clear import clearscreen
import random
import time

def set_difficulty():
    game_mode = {'hard': 5, 'easy': 10}
    choice = input("Which mode do you want to play? Enter 'hard' for 5 guesses or 'easy' for 10 guesses: ")
    number_of_guesses = game_mode[choice]
    return number_of_guesses

def guess_check(num1, num2):
    """
    input: Two integer numbers (number1 and number2)
    output: output whether the number1 is too high, too low or equal with number2
    """
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
    number_of_guesses = set_difficulty()
    computer_guess = random.randint(1,100)
    
    game_over =  False
    while game_over == False:
        print(f"You have {number_of_guesses} guesses left.")
        user_guess = int(input("Guess your number: "))

        while guess_check(user_guess, computer_guess) != "Correct":
            print(guess_check(user_guess, computer_guess))
            number_of_guesses -= 1
            if number_of_guesses == 0:
                break
            print(f"You have {number_of_guesses} guesses left.")
            user_guess = int(input("Guess your number: "))
        
        if guess_check(user_guess, computer_guess) == "Correct":
            print(f"Congratulations. You guessed correctly. The number is {user_guess}")
            break
        else:
            print("You ran out of guesses. You lose")
            break

    to_continue = input("Do you want to start a new game? Type 'y' for yes and 'n' for no: ")