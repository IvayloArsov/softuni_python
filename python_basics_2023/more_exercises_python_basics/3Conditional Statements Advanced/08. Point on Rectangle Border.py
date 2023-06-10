x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x == x1 or x == x2:
    if y2 >= abs(y) >= y1:
        print('Border')
    else:
        print('Inside / Outside')
elif y == y1 or y == y2:
    if x2 >= abs(x) >= x1:
        print('Border')
    else:
        print('Inside / Outside')
else:
    print('Inside / Outside')