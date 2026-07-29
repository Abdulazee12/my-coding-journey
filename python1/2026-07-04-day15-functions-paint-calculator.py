# ================================
# Date: July 4, 2026
# Day: Day 15
# Topic: Functions - Paint Calculator Exercise
# Source: Angela Yu - 100 Days of Code (Day 8)
# ================================

# What I learned from this exercise:
# - Function parameters must match the keyword argument 
#   names used when calling the function
# - Variables inside a function must use the parameter 
#   names, not the outside variable names
# - import math gives access to math.ceil() which always 
#   rounds UP to the nearest whole number
# - math.ceil() is better than round() when you always 
#   need to round up (like buying paint cans)

import math
def paint_calc(height, width, cover):
    num_cans = math.ceil(height * width / cover)
    print(f"You'll need {num_cans} cans of paint.")


# Don't change the code below
test_h = int(input("Height of the Wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
