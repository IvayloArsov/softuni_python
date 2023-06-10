hour = int(input())
minute = int(input())

if minute <= 44:
    minute += 15
    print(f'{hour}:{minute}')
else:
    hour += 1
    minute += 15
    if hour > 23:
        hour = 0
    if 60 <= minute < 70:
        print(f'{hour}:0{minute-60}')
    else:
        print(f'{hour}:{minute-60}')