while True:
    command = input()
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    if len(command) == 5:
        print(f"{command} goes to Slytherin.")
    if len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    if len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
