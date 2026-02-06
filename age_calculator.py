# Ask user for birth year
birth_year_input = input("Enter your birth year: ")

# Explicit type conversion
birth_year = int(birth_year_input)

# Current year is 2026
current_year = 2026

# Calculate age
age = current_year - birth_year

# Print result
print(f"You are {age} years old.")
