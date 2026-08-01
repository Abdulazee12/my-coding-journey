# ================================
# Date: July 4, 2026
# Day: Day 15
# Topic: Functions - Prime Checker Exercise
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned from this exercise:
# - Used a for loop with range(2, number) to check 
#   every possible divisor
# - % operator returns 0 when a number divides evenly
# - break exits the loop immediately when a divisor is found
# - for/else runs the else block ONLY if break never fired
#   meaning no divisor was found = number is prime


# # # Another Challenge
# # # Write your code below this line
# # def prime_checker(number):
# #     for i in range(2, number):
# #         if number % i == 0:
# #             print("It's not a prime number.")
# #             break
# #     else:
# #         print("It's a prime number.")

# # # Do NOT change any of the code below
# # n = int(input("Check this number: "))
# # prime_checker(number=n)