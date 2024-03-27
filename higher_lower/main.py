#higher lower game
from art import logo, vs
from clear import clearscreen
from game_data import data
import random

#helper functions
def deserialise(dict):
    """
    deserialise the dictionary to get the name, follower count etc.
    returns name, follower_count, description and country
    """
    name = dict['name']
    follower_count = dict['follower_count']
    description = dict['description']
    country = dict['country']

    return name, follower_count, description, country

def print_dict(name, description, country):
    """
    prints the item in the required format 
    """
    return f"{name}, a {description}, from {country}."
    
def compare(follower_count1, follower_count2):
    """
    returns true if follower count1 is greater than follower count2
    """
    return follower_count1 > follower_count2

def generate_choices(length):
    """
    generates the random choices required 
    """
    choice1 = random.randint(0,length)
    choice2 = random.randint(0,length)
    while choice2 == choice1:
        choice2 = random.randint(0,length)
    
    return choice1, choice2

def print_choices(choice1, choice2):
    """"
    prints the two choices to the user
    """
    name1, follower_count1, description1, country1 = deserialise(data[choice1])
    print(f"Choice A: {print_dict(name1, description1, country1)}")
    print(vs) 
    name2, follower_count2, description2, country2 = deserialise(data[choice2])
    print(f"Choice B: {print_dict(name2, description2, country2)}")
    return follower_count1, follower_count2

#game start
length = len(data)
user_score = 0

#recursive game function
def high_low_game():
    global user_score

    #generate and print choices to the user
    choice1, choice2 = generate_choices(length-1)
    follower_count1, follower_count2 = print_choices(choice1, choice2)

    user_guess = input("Who has more followers? Type A or B: ")

    if (user_guess.lower() == 'a' and compare(follower_count1, follower_count2)) or (user_guess.lower() =='b' and not compare(follower_count1, follower_count2)):
        user_score += 1
        high_low_game()
    else: 
        clearscreen()
        print(logo)
        print(f"Sorry that's wrong. Your score is: {user_score}")

clearscreen()
print(logo)
high_low_game()