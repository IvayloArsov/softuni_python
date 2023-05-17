import math

h_wall = int(input())
w_wall = int(input())
unpainted = int(input())

area = (h_wall*w_wall*4)
area = math.ceil(area* (1-unpainted/100))

while True:
    command = input()

    if command == "Tired!":
        print(f'{area} quadratic m left.')
        break
    paint = int(command)

    if area > paint:
        area -= paint

    elif paint > area:
        print(f'All walls are painted and you have {(paint-area)} l paint left!')
        break

    elif paint == area:
        print(f'All walls are painted! Great job, Pesho!')
        break

