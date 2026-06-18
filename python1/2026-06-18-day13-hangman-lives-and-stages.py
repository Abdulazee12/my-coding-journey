# ================================
# Date: June 18, 2026
# Topic: While Loops, break, Lists, Hangman Game (completed)
# Source: Angela Yu - 100 Days of Code (Day 7) - Hangman Challenge
# ================================

# What I learned today:
# - Finished wiring up 'lives' to decrease on wrong guesses
# - Learned two different ways to end a while loop early:
#   1) Building the stop condition directly into the while line
#      (while "_" in display and lives > 0)
#   2) Using 'break' inside an if statement to exit immediately,
#      even while the while condition is still technically True
#      (while True style logic - break is the ONLY way out)
# - Learned that 'break' stops a loop instantly, regardless of
#   what the loop's own condition says
# - Used 'lives' itself as a list index (stages[lives]) to show
#   the correct ASCII art stage automatically as lives decrease -
#   no hardcoding needed, since the index updates with the game
# - Fixed SyntaxWarning issues caused by single backslashes (\)
#   in my ASCII art strings by escaping them properly (\\)
# - Practiced deciding WHERE inside a loop a piece of logic should
#   run - during every iteration vs only once after the loop ends

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




lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')



#Create blanks
display = []
for letter in chosen_word:
    display.append("_")


# ============================================
# APPROACH 1: Loop condition checks lives directly
# ============================================

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    for position in range(0, len(chosen_word)):
        # print(f"Current position: {position}\n Current letter: {chosen_word[position]}\n Guessed letter: {guess}")
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    
    if guess not in chosen_word:
        lives -= 1
           
    print(stages[lives])
    print(f"{''.join(display)}")

if lives == 0:
    print(f"You've lost.\n Game Ended!")
else:
    print("You won")


# ============================================
# APPROACH 2: Using break to exit early when lives hit 0
# ============================================
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     for position in range(0, len(chosen_word)):
#         if chosen_word[position] == guess:
#             display[position] = chosen_word[position]

#     if guess not in chosen_word:
#         lives -= 1

#     if lives == 0:
#         break

#     print(f"{''.join(display)}")

# if lives == 0:
#     print("You lost")
# else:
#     print("You won")
