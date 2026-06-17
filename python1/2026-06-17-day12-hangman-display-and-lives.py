# ================================
# Date: June 17, 2026
# Topic: While Loops, Lists, Strings, Hangman Game
# Source: Angela Yu - 100 Days of Code (Day 7) - Hangman Challenge
# ================================

# What I learned today:
# - Built the core guessing logic for the Hangman game
# - Created an empty 'display' list with underscores 
#   representing each letter in the chosen word
# - Used range(len(chosen_word)) to loop through positions 
#   (not letters directly), since I needed the index to 
#   update both chosen_word and display at the same spot
# - Learned the difference between looping through values 
#   (for letter in chosen_word) vs looping through positions 
#   (for position in range(len(chosen_word)))
# - Used "_" in display as a while loop condition to keep 
#   the game running until the word is fully guessed
# - Learned that strings are immutable in Python - you can't 
#   do chosen_word[i] = something, but you CAN do that on lists
# - Used ''.join(display) to turn the list of letters/underscores 
#   back into a readable string
# - Set up a 'lives' variable and ASCII art 'stages' list ready 
#   for tracking wrong guesses (not wired up yet - next session)

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


#TODO-5 - Create a variable called 'lives' to keep track of the 
# number of lives left. 
# Set 'lives' to equal 6.

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')



#Create blanks
display = []
for letter in chosen_word:
    display.append("_")



while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(0, len(chosen_word)):
        # print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed letter: {guess}")
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    #TODO-2: - If guess is not a letter in the chosen_word, 
    # Then reduce 'lives' by 1.If lives goes down to 0 and 
    # then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{''.join(display)}")

    #Check if user has got all letters.
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the 
    # current number of 'lives' the user has remaining.

    print(display)
print("You've won!")

