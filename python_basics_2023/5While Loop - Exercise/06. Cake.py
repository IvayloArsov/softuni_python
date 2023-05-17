a = int(input())
b = int(input())
pieces = a * b
taken = ''

while True:
    taken = input()

    if taken == 'STOP':
        print(f'{abs(pieces)} pieces are left.')
        break
    elif int(taken) >= pieces:
        print(f'No more cake left! You need {abs(int(taken)-pieces)} pieces more.')
        break

    pieces -= int(taken)