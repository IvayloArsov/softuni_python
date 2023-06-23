# initialize empty dictionary
users = dict()
while True:
    command = input()
    if command == "End":
        break
    company, name = command.split(" -> ")
    # initialize empty list for the course in the input, if it doesn't exist
    if company not in users:
        users[company] = []
    # append the name to the list if it doesn't already exist
    if name not in users[company]:
        users[company].append(name)

# nested for loop to print out the ledger according ot the requirements
for company, user in users.items():
    print(f"{company}")
    for student in user:
        print(f"-- {student}")