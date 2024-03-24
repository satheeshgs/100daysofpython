#auction
import time
from clear import clearscreen
from art import logo
#Step 1: Print logo
print(logo)

new_bidder = "yes"
bidders = {}
#Step 2: ask for name and bid as long as there is a bidder
while new_bidder == "yes": 
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'")
    if new_bidder == "yes":
        clearscreen()

#Step 3: Calculate highest bidder
highest_bidder = max(bidders, key = lambda x: bidders[x])  

#Step 4: Display result 
print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")