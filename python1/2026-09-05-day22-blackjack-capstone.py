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

def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0

    score = sum(hand)

    if score > 21 and 11 in hand:
        score -= 10
    return score

def blackjack():
    user_cards = deal_card()
    computer_cards = deal_card()
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
        if another_card == 'y':
            user_cards.append(random.choice(cards))
            user_score = calculate_score(user_cards)
            if user_score > 21:
                break
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
        elif another_card == 'n':
            break
    

blackjack()