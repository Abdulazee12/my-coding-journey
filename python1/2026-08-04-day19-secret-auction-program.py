# ================================
# Date: August 4, 2026
# Day: Day 19
# Topic: Secret Auction Program
# Source: Angela Yu - 100 Days of Code (Day 9)
# ================================

# What I learned today:
# - Used while True: to keep looping indefinitely
#   until the user types 'no' (break is the only exit)
# - while True: is used when you don't know upfront
#   how many times the loop needs to run
# - Stored bidder names and amounts in a dictionary
#   bidding_dictionary[name] = bid
# - Looped through dictionary to find highest bid
#   using highest_bid = 0 and winner = "" as starting values
# - Used os.system("cls") to clear screen between bidders
#   so bids stay secret from other bidders
# - Replaced from replit import clear with import os

import os
# from art import logo
# print(logo)    

bidding_dictionary = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidding_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if other_bidders == "yes":
        os.system("cls")
    elif other_bidders == "no":
        break

highest_bid = 0
winner = ""
for bidder in bidding_dictionary:
    bid_amount = bidding_dictionary[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(bidding_dictionary)
print(f"The winner is {winner} with a bid of ${highest_bid}")