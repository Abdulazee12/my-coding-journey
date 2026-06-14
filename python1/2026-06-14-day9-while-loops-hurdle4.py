# ================================
# Date: June 14, 2026
# Topic: While Loops + Custom Functions
# Source: Angela Yu - 100 Days of Code (Day 6/7)
# Challenge: Reeborg's World - Hurdle 4
# ================================

# What I learned today:
# - Hurdle 4 introduced walls of varying/unknown length
# - Used while loops INSIDE jump() to handle this:
#   - while wall_on_right(): move()  -> keep moving 
#     along the wall until it ends
#   - while front_is_clear(): move() -> move forward
#     until reaching the next wall/edge
# - This makes jump() flexible enough to handle 
#   hurdles of different sizes, not just fixed ones

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
        
# while not at_goal():
#     if wall_in_front():
#         jump()    
#     else:
#         move()

