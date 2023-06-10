capacity = int(input())
attendants = int(input())
a = 0
b = 0
v = 0
g = 0
for i in range(0, attendants):
    command = input()
    if command == 'A':
        a += 1
    elif command == 'B':
        b += 1
    elif command == 'V':
        v += 1
    elif command == 'G':
        g += 1

print(f'{a / attendants * 100:.2f}%')
print(f'{b / attendants * 100:.2f}%')
print(f'{v / attendants * 100:.2f}%')
print(f'{g / attendants * 100:.2f}%')
print(f'{attendants / capacity * 100:.2f}%')
