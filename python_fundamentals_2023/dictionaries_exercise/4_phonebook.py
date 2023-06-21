# construct empty dictionary to hold future input values
phonebook = {}

while True:
    command = input()
    if command.isdigit():
        # variable n holds the number of searches that will be performed
        n = int(command)
        break

    name, number = command.split("-")
    # add the name and number to the phonebook dictionary, if already exists - updates it
    phonebook[name] = phonebook.get(number, number)


# for loop for checking the phonebook dictionary for hits
for _ in range(n):
    search = input()
    # check if the searched name is in the phonebook dictionary key
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
