# initialize empty dictionary
ledger = dict()
while True:
    command = input()
    if command == "end":
        break
    course, name = command.split(" : ")
    # initialize empty list for the course in the input, if it doesn't exist
    if course not in ledger:
        ledger[course] = []
    # append the name to the list
    ledger[course].append(name)

# nested for loop to print out the ledger according ot the requirements
for course_name, students in ledger.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")
