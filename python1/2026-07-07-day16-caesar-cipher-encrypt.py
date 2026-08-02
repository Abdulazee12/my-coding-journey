# ================================
# Date: July 7, 2026
# Day: Day 16
# Topic: Caesar Cipher - Encrypt Function
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned today:
# - ord() converts a character to its ASCII number
#   e.g. ord("a") = 97, ord("h") = 104
# - chr() converts a number back to a character
#   e.g. chr(109) = "m"
# - Combined ord() and chr() to shift letters forward
#   in the alphabet by a given shift amount
# - Used ''.join() to combine a list of letters 
#   into a single string (same as Hangman)
# - Used if/else to call encrypt() or decrypt()
#   based on user's direction input
# - decrypt() function still to be built next session

# # alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
#             'n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#     cipher_text = []
#     for letter in text:
#         cipher_text.append(chr(ord(letter) + shift))
#     print(f"The encoded text is {''.join(cipher_text)}")
    
# encrypt(text,shift)