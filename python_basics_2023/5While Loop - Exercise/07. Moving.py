a = int(input())
b = int(input())
c = int(input())
room = a*b*c
taken_space = ''

while True:
    taken_space = input()

    if taken_space == 'Done':
        print(f'{room} Cubic meters left.')
        break
    elif int(taken_space) >= room:
        print(f'No more free space! You need {abs(int(taken_space)-room)} Cubic meters more.')
        break
    room -= int(taken_space)
