# ================================
# Date: September 5, 2026
# Day: Day 22
# Topic: Blackjack Capstone Project - Part 1
# Source: Angela Yu - 100 Days of Code (Day 11)
# ================================

# What I built today:
# - Created a deal_card() function that deals 2 random cards
# - Function creates its own empty hand list
# - Uses a for loop with range(0, 2) to pick 2 random cards
# - Returns the hand list to whoever called it
# - Called deal_card() twice — once for user, once for computer
# - Each player gets their own separate list of 2 cards
# - Key insight: deal_card() doesn't know who it's dealing to
#   it just deals 2 cards and hands them back (reusable!)

# Still to build:
# - calculate_score() function
# - Blackjack detection
# - Ace handling (11 or 1)
# - User hit or stand logic
# - Computer drawing logic
# - Win/loss/draw comparison

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    hand = []
    for i in range(0, 2):
        hand.append(random.choice(cards))
    return hand

user_cards = deal_card()
computer_cards = deal_card()

print(user_cards)
print(computer_cards)