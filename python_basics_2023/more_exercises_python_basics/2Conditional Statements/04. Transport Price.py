n = int(input())
time_of_day = input()

if n >= 100:
    print(f'{n*0.06:.2f}')
elif n >= 20:
    print(f'{n*0.09:.2f}')
else:
    if time_of_day == 'day':
        print(f'{n*0.79+0.70:.2f}')
    elif time_of_day == 'night':
        print(f'{n*0.90+0.70:.2f}')
