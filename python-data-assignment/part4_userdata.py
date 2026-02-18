def calculate_average(users):
    for user in users:
        avg = sum(user["scores"]) / len(user["scores"])
        user["average"] = avg
    return users


def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 78],
            "roles": {"viewer"}
        }
    ]

    users = calculate_average(users)

    for user in users:
        print("Name:", user["name"])
        print("Average Score:", user["average"])
        print("Admin Access:", has_admin_access(user["roles"]))
        print("-------------------")


main()
