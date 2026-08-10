# ================================
# Date: August 6, 2026
# Day: Day 21
# Topic: Calculator with while loop
# Source: Angela Yu - 100 Days of Code (Day 10/11)
# ================================

# What I learned from this challenge:
# - Stored functions as VALUES inside a dictionary:
#   operations = {"+": add, "-": subtract ...}
# - Called a function from a dictionary:
#   calculation_function = operations[operation_symbol]
#   latest_answer = calculation_function(num1, num2)
# - Used should_continue = True with while loop
#   instead of while True: + break
# - "y" needs NO special code - loop naturally continues
# - Only "n" needs handling: should_continue = False
# - num1 = latest_answer carries result into next calculation
#   so the previous answer becomes the new first number
# - Looped through dictionary keys to display operations:
#   for symbol in operations: print(symbol)

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
}
        
num1 = int(input("What's the first number?: "))

should_continue = True
while should_continue:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    latest_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {latest_answer}") 

    num1 = latest_answer
    cont_ex = (input(f"Type 'y' to continue calculating with {num1}, or type 'n' to exit.: "))
    if cont_ex == "n".lower():
        should_continue = False
