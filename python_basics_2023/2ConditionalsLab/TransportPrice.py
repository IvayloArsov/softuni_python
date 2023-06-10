# 'n' is kilometers that need to be travelled
n = int(input())
m = input()


if n >= 100:
    print(n*0.06)
elif n >= 20:
    print(n*0.09)
else:
    if m == 'day':
        print((n*0.79)+0.70)
    elif m == 'night':
        print((n*0.90)+0.70)