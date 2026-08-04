# ================================
# Date: August 4, 2026
# Day: Day 18
# Topic: Dictionaries - Travel Log Challenge
# Source: Angela Yu - 100 Days of Code (Day 9)
# ================================

# What I learned today:
# - A list can contain dictionaries as items
# - Each dictionary in the list has the same structure
#   (same keys, different values)
# - Created a function to add a new dictionary to a list
# - Used parameters instead of hardcoded values so the
#   function works for ANY country, not just Russia
# - travel_log.append(new_country) adds the new dictionary
#   to the end of the list
# - Underscore _ in parameter names matters - 
#   cities_visited ≠ cities visited (space causes SyntaxError)

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,    
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

# DO NOT change the code above

# Write the function that will allow new countries 
def add_new_country(country, visits, cities_visited):
    new_country = {
        "country": country,
        "visits": visits,
        "cities_visited": cities_visited,
    }
    travel_log.append(new_country)


add_new_country(country = "Russia", visits = 2, cities_visited = ["Moscow", "Saint Petersburg"])

# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)