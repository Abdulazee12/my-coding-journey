# ================================
# Date: July 3, 2026
# Day: Day 15
# Topic: Functions and Arguments
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned today:
# 1. How to define a simple function using def
# 2. Functions with one parameter (input)
# 3. Functions with more than one parameter
# 4. Positional arguments vs Keyword arguments
#    - Positional: order matters, switching changes meaning
#    - Keyword: you specify which parameter gets which value
#      so order doesn't matter anymore

# DAY 08
# Simple function
# def greet():
#     print("Good morning!")
#     print("Good afternoon!")
#     print("Good evening!")

# greet()

# Function that allows for input

# def greet_name(name):
#     print(f"Good morning {name}")
#     print(f"Good afternoon {name}")

# greet_name("Ayomide")

# Functions with more than 1 input
# def greet_twopams(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# Positional Argument - when we switch both parameters and 
# their arguments also changes.
#  Keyword Arguments helps solve problems with positional argument

# greet_twopams("Ayo","London")

# Function with keyword arguments
def greet_key(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_key(location = "London", name = "Ayomide")