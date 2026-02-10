balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified (True/False): ")

if verified_input == "True":
    verified = True
elif verified_input == "False":
    verified = False
else:
    print("Invalid verification input")
    exit()

if verified and withdraw <= balance:
    print("Transaction successful")
else:
    print("Transaction denied")
