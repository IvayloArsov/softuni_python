deg = float(input())

if 26.00 <= deg <= 35.00:
    print('Hot')
elif 20.1 <= deg <= 25.90:
    print('Warm')
elif 15.00 <= deg <= 20.00:
    print('Mild')
elif 12 <= deg <= 14.9:
    print('Cool')
elif 5 <= deg <= 11.9:
    print('Cold')
else:
    print('unknown')