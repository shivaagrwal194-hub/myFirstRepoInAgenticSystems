# Ask for name
name = input("Enter your name: ")

# Ask for age
age_input = input("Enter your age: ")
age = int(age_input)

# Ask active status
active_input = input("Are you an active user (True/False): ")
is_active = active_input == "True"

# Print summary
print(f"User {name} is {age} years old. Active status: {is_active}")

