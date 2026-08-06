# ================================
# Date: August 4, 2026
# Day: Day 20
# Topic: Functions returning values - Days in Month
# Source: Angela Yu - 100 Days of Code (Day 10)
# ================================

# What I learned today:
# - return sends a value back from a function so other
#   parts of code can USE it, unlike print which just displays
# - is_leap() was changed from print to return True/False
#   so days_in_month() could use its result directly
# - Called one function inside another: is_leap(year)
#   used inside days_in_month() to check leap year
# - Used month - 1 to convert month number to list index
#   because lists start at 0 but months start at 1
# - Combined two conditions with 'and':
#   if is_leap(year) and month == 2: return 29

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True
    else:
        return False    

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


# Do Not change the code below
year = int(input("Enter a year: ")) 
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)