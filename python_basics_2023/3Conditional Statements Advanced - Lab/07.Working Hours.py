hour = int(input())
day = input()
work_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]
work_hours = list(range(10,19))
if day in work_days:
    if hour in work_hours:
        print('open')
    else:
        print('closed')
else:
    print('closed')