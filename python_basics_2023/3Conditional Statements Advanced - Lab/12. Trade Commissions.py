city = input()
sales = float(input())
commission = 0
cities = [
    'Sofia',
    'Varna',
    'Plovdiv',
]
if 0 > sales:
    print('error')
elif city in cities:
    if city == 'Sofia':
        if sales > 10_000:
            commission = sales*0.12
            print(f'{commission:.2f}')
        elif sales > 1_000:
            commission = sales * 0.08
            print(f'{commission:.2f}')
        elif sales > 500:
            commission = sales * 0.07
            print(f'{commission:.2f}')
        elif sales >= 0:
            commission = sales * 0.05
            print(f'{commission:.2f}')
    elif city == 'Varna':
        if sales > 10_000:
            commission = sales*0.13
            print(f'{commission:.2f}')
        elif sales > 1_000:
            commission = sales * 0.10
            print(f'{commission:.2f}')
        elif sales > 500:
            commission = sales * 0.075
            print(f'{commission:.2f}')
        elif sales >= 0:
            commission = sales * 0.045
            print(f'{commission:.2f}')
    elif city == 'Plovdiv':
        if sales > 10_000:
            commission = sales*0.145
            print(f'{commission:.2f}')
        elif sales > 1_000:
            commission = sales * 0.12
            print(f'{commission:.2f}')
        elif sales > 500:
            commission = sales * 0.08
            print(f'{commission:.2f}')
        elif sales >= 0:
            commission = sales * 0.055
            print(f'{commission:.2f}')
else:
    print('error')