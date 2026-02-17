def greet_student(name):
    return "Hello, " + name

def calculate_scores(scores):
    total_subjects = len(scores)
    average = sum(scores) / total_subjects
    return total_subjects, average

def get_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Alice"
    scores = [60, 70, 65]

    greeting = greet_student(name)
    subjects, average = calculate_scores(scores)
    result = get_result(average)

    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)

main()
