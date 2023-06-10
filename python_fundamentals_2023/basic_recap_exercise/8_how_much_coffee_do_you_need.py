events = ['coding', 'dog', 'cat', 'movie']
coffees = 0
while True:
    command = input()
    if command == "END":
        break
    for element in events:
        if element.lower() == command:
            coffees += 1
        elif element.upper() == command:
            coffees += 2
        else:
            continue
if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")

