age = float(input())
sex = input()


if age >=16:
    if sex == 'm':
        print('Mr.')
    elif sex == 'f':
        print('Ms.')
else:
    if sex == 'm':
        print('Master')
    elif sex == 'f':
        print('Miss')