from collections import deque
liters = int(input())
users = deque()
name = input()
while name != "Start":
    users.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        person_name = users.popleft()

        if liters_to_give <= liters:
            liters -= liters_to_give
            print(person_name, "got water")
        else:
            print(person_name, "must wait")
    else:
        liters_to_add = int(data[1])
        liters += liters_to_add


    command = input()


print(f"{liters} liters left")