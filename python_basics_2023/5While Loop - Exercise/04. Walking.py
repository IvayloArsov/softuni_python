goal = 10_000
steps_counter = 0
steps = ''

while True:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        steps_counter += steps
        if steps_counter >= goal:
            print(f'Goal reached! Good job!\n{steps_counter - goal} steps over the goal!')
        else:
            print(f'{goal - steps_counter} more steps to reach goal.')
        break

    steps_counter += int(steps)
    if steps_counter >= goal:
        print(f'Goal reached! Good job!\n{steps_counter - goal} steps over the goal!')
        break
