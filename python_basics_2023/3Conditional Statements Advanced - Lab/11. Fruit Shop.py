fruit = input()
day = input()
quantity = float(input())
price = 0
work_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]
weekend = [
    'Saturday',
    'Sunday'
]

price_workdays = {'banana': 2.50,
                  'apple': 1.20,
                  'orange': 0.85,
                  'grapefruit': 1.45,
                  'kiwi': 2.70,
                  'pineapple': 5.50,
                  'grapes': 3.85
                  }
price_weekend = {'banana': 2.70,
                 'apple': 1.25,
                 'orange': 0.90,
                 'grapefruit': 1.60,
                 'kiwi': 3.00,
                 'pineapple': 5.60,
                 'grapes': 4.20
                 }
if day in work_days:
    if fruit in price_workdays.keys():
        print(f'{price_workdays[fruit] * quantity:.2f}')
    else:
        print('error')
elif day in weekend:
    if fruit in price_weekend.keys():
        print(f'{price_weekend[fruit] * quantity:.2f}')
    else:
        print('error')
else:
    print('error')
