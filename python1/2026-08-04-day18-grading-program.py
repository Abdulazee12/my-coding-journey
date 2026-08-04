# ================================
# Date: August 4, 2026
# Day: Day 18
# Topic: Dictionaries - Grading Program
# Source: Angela Yu - 100 Days of Code (Day 9)
# ================================

# What I learned today:
# - Looping through a dictionary with 'for key in dict'
#   only gives you keys, not values
# - Access values inside loop using dict[key]
# - Used if/elif to assign grades based on score ranges
# - Added "Outstanding" for scores above 90 as own improvement
# - Added results to a NEW dictionary (student_grades)
#   instead of modifying the original (student_scores)

student_scores = {
"Harry": 81,
"Ron": 78,  
"Herminone": 99,
"Braco": 74,
"Neville": 62,
}

# Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for keys in student_scores: 
    if student_scores[keys] >= 91 and student_scores[keys] <= 100:
        student_grades[keys] = "Outstanding"
    elif student_scores[keys] >= 81 and student_scores[keys] <= 90:
        student_grades[keys] = "Exceeds Expectations"
    elif student_scores[keys] >= 71 and student_scores[keys] <= 80:
        student_grades[keys] = "Acceptable"
    elif student_scores[keys] <= 70:
        student_grades[keys] = "Fail"

# Don't change the code below 👇
print(student_grades)