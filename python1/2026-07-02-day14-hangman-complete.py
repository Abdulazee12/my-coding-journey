# ================================
# Date: July 2, 2026
# Day: Day 14
# Topic: Hangman Game - Complete
# Source: Angela Yu - 100 Days of Code (Day 7)
# ================================

# Completed the full Hangman game today.
# Will add detailed notes later.

# import random

# from hangman_words import word_list
# from hangman_art import stages, logo
# import os

# print(logo)

# chosen_word = random.choice(word_list)

# lives = 6


# #Create blanks
# display = []
# for letter in chosen_word:
#     display.append("_")


# while "_" in display and lives > 0:
#     guess = input("Guess a letter: ").lower()

#     os.system("cls")

#     if guess in display:
#         print(f"You've already entered the letter {guess}")

#     for position in range(0, len(chosen_word)):
#         # print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed letter: {guess}")
#         if chosen_word[position] == guess:
#             display[position] = chosen_word[position]

    
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life")

#     if guess not in chosen_word:
#         lives -= 1
           
#     print(stages[lives])
#     print(f"{''.join(display)}")

# if lives == 0:
#     print(f"You've lost.\n Game Ended!")
# else:
#     print("You won")

