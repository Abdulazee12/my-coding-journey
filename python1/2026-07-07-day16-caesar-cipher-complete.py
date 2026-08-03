# ================================
# Date: July 7, 2026
# Day: Day 16
# Topic: Caesar Cipher - Complete (Encrypt + Decrypt)
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned today:
# - ord() and chr() for character/number conversion
# - Used alphabet list + .index() to find letter positions
# - % 26 handles wraparound when shift goes beyond "z"
#   e.g. z(25) + 5 = 30 → 30 % 26 = 4 → "e"
# - encrypt() shifts letters FORWARD by shift amount
# - decrypt() shifts letters BACKWARD by shift amount
# - Built decrypt() independently without guidance!
# - if/else calls correct function based on user direction

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text = []
    for letter in text:
        shifted_position = (alphabet.index(letter) + shift) % 26
        cipher_text.append(alphabet[shifted_position])
    print(f"The encoded text is {''.join(cipher_text)}")


def decrypt(text, shift):
    cipher_text = []
    for letter in text:
        shifted_position = (alphabet.index(letter) - shift) % 26
        cipher_text.append(alphabet[shifted_position])
    print(f"The decoded text is {''.join(cipher_text)}")

if direction == "encode":
    encrypt(text,shift)
else: 
    decrypt(text, shift)