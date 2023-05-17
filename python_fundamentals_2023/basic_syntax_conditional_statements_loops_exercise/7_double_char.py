while True:
    command = input()
    if command == 'End':
        break
    if command == "SoftUni":
        continue
    for char in command:
        print(char*2, end="")
    print()


