from collections import deque

prog_time = deque(map(int, input().split()))
tasks = list(map(int, input().split()))

ducks = {
    "Darth Vader Ducky": 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while prog_time and tasks:
    current_time = prog_time.popleft()
    current_tasks = tasks.pop()
    result = current_tasks * current_time

    if result <= 60:
        ducks['Darth Vader Ducky'] += 1
    elif result <= 120:
        ducks['Thor Ducky'] += 1
    elif result <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
    elif result <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
    else:
        current_tasks -= 2
        tasks.append(current_tasks)
        prog_time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f'Darth Vader Ducky: {ducks["Darth Vader Ducky"]}')
print(f'Thor Ducky: {ducks["Thor Ducky"]}')
print(f'Big Blue Rubber Ducky: {ducks["Big Blue Rubber Ducky"]}')
print(f'Small Yellow Rubber Ducky: {ducks["Small Yellow Rubber Ducky"]}')

