n1 = int(input())
n2 = int(input())
opr = input()
result = 0
if opr == '+':
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} {opr} {n2} = {result} - even')
    else:
        print(f'{n1} {opr} {n2} = {result} - odd')

elif opr == '-':
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} {opr} {n2} = {result} - even')
    else:
        print(f'{n1} {opr} {n2} = {result} - odd')

elif opr == '*':
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {opr} {n2} = {result} - even')
    else:
        print(f'{n1} {opr} {n2} = {result} - odd')

elif opr == '/':
    if n2 > 0:
        result = n1 / n2
        print(f'{n1} {opr} {n2} = {result:.2f}')
    else:
        print(f'Cannot divide {n1} by zero')

elif opr == '%':
    if n2 > 0:
        result = n1 % n2
        print(f'{n1} {opr} {n2} = {result}')
    else:
        print(f'Cannot divide {n1} by zero')
