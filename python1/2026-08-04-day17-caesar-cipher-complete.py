# ================================
# Date: August 4, 2026
# Day: Day 17
# Topic: Caesar Cipher - Fully Complete
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned today:
# - Combined encrypt() and decrypt() into caesar() function
# - Used ternary operator inside print() for dynamic messages
# - shift_amount %= 26 normalises large shift numbers
# - Used if letter in alphabet to handle spaces/numbers/symbols
# - Learned recursion - a function that calls itself
#   start() calls start() again if user types 'yes'
# - Used .lower() on play_again input to handle uppercase YES
# - print("Goodbye!") runs when user types 'no' ending the game

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# from art import logo
# print(logo)

def caesar(plain_text, shift_amount, direction):
    cipher_text = []
    shift_amount %= 26
    for letter in plain_text:
        if letter in alphabet:
            if direction == "encode":
                shifted_position = (alphabet.index(letter) + shift_amount) % 26
                cipher_text.append(alphabet[shifted_position])
            elif direction == "decode":
                shifted_position = (alphabet.index(letter) - shift_amount) % 26
                cipher_text.append(alphabet[shifted_position])
        else:
            cipher_text.append(letter)
    print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is {''.join(cipher_text)}")


def start(): 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text = text, shift_amount = shift, direction = direction)
    play_again = input("Do you want to play again? Type 'yes' or 'no'. \n")
    if play_again.lower() == 'yes':
        start()
    else:
        print("Goodbye!")
start()

