import sys

inpt = input()
minnum = sys.maxsize

while inpt != 'Stop':
    num = int(inpt)
    if num < minnum:
        minnum = num
    inpt = input()

print(minnum)
