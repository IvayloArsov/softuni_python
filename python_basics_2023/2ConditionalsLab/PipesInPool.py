import math

v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

water = (p1+p2)*h

if water <= v:
    print(f'The pool is {math.trunc((water/v)*100)}% full. Pipe 1: {math.trunc((p1*h)/water*100)}%. Pipe 2: {math.trunc((p2*h)/water*100)}%.')
else:
    print(f'For {h} hours the pool overflows with {water-v} liters.')
