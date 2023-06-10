shape = input('Type the type of shape: square, rectangle, circle or triangle:')
if shape == 'square':
    a = float(input())
    print(f'{a*a:.3f}')
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a*b:.3f}')
elif shape == 'circle':
    from math import pi
    a = float(input())
    print(f'{a*a*pi:.3f}')
elif shape == 'triangle':
    a = float(input())
    b = float(input())
    print(f'{a*b*0.5:.3f}')