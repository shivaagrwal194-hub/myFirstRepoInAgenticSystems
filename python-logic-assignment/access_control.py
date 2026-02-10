
age = int(input("Enter your age: "))
has_id_input = input("Do you have ID (True/False): ")

if has_id_input == "True":
    has_id = True
elif has_id_input == "False":
    has_id = False
else:
    print("Invalid ID input")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
