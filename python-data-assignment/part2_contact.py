contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Sohan": "9988776655"
}

print("All Contacts:")
for name in contacts:
    print(name, ":", contacts[name])

search_name = input("Enter name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")
