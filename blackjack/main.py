############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random 
from art import logo
from clear import clearscreen
#from helpers import sum_of_cards, determine_blackjack, determine_bust
#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    choice = random.randint(0,12)
    return cards[choice]
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def sum_of_cards(cards_list):
    if 11 in cards_list:
        if sum(cards_list) > 21: 
            cards_list[cards_list.index(11)] = 1
    
    return int(sum(cards_list))

def determine_blackjack(cards_list):
    return sum_of_cards(cards_list) == 21



def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    
    #getting the user cards 
    draw_new_card = 'y'
    user_score = sum_of_cards(user_cards)
    while draw_new_card == 'y' and user_score <= 21:
        #display user cards 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        draw_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        #user's choice to draw cards 
        if draw_new_card == 'y':
            user_cards.append(deal_card())
            user_score = sum_of_cards(user_cards)
        else:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
        
    #Computer draws cards until it reached 16 or higher
    computer_score = sum_of_cards(computer_cards)
    while computer_score < 16: 
        computer_cards.append(deal_card())
        computer_score = sum_of_cards(computer_cards)
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        
    #score comparisons and blackjack
    if user_score > 21:
        print("You went over. You lose :')")
    elif user_score == computer_score:
        print("It's a draw")
    elif determine_blackjack(user_cards):
        print("You won. It's a blackjack :) ")
    elif determine_blackjack(computer_cards):
        print("Opponent has blackjack: You lost :( )")
    elif (user_score > computer_score) or (computer_score > 21): 
        print("You won")
    else:
        print("You lost")

continue_game = 'y'

while continue_game == 'y':
    blackjack()
    continue_game = input("Do you want to play a game of Blackjack. Type 'y' or 'n': ")