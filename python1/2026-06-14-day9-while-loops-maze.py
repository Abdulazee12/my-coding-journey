# ================================
# Date: June 14, 2026
# Topic: While Loops + Conditionals
# Source: Angela Yu - 100 Days of Code (Day 6/7)
# Challenge: Reeborg's World - Maze
# ================================

# What I learned today:
# - This challenge used the "right-hand rule" for 
#   solving mazes — a classic algorithm
# - Priority order matters: check right first, 
#   then front, then turn left as last resort
# - elif allows checking multiple conditions in order,
#   only one branch runs per loop cycle
# - Combining right_is_clear(), front_is_clear(), 
#   and turn_left() lets the robot navigate any maze 
#   without knowing its layout in advance

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

