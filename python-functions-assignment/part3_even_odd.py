def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# calling function
result = check_even_odd(4)
print("Number is", result)
