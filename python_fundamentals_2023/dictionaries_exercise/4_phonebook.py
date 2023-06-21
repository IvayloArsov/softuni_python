# construct empty dictionary to hold future input values
phonebook = {}
# while loop that receives input values for the phonebook dictionary
while True:
    command = input()
    # if an integer is received, the loop breaks
    if command.isdigit():
        # variable n holds the number of searches that will be performed
        n = int(command)
        break

    # split the command input into Name and Phonenumber
    name, number = command.split("-")
    # add the name and number to the phonebook dictionary
    phonebook[name] = phonebook.get(number, 0)
    # update the phonebook dictionary with the new number
    phonebook[name] = number

# for loop for checking the phonebook dictionary for hits
for _ in range(n):
    # user input that is used to search the phonebook dictionary
    search = input()
    # boolean check if the searched name is in the phonebook dictionary key
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    # if the search is not in the phonebook dictionary, print out error messenger
    else:
        print(f"Contact {search} does not exist.")
