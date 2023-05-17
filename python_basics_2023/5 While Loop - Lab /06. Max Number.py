import sys

inpt = input()
mxnum = -sys.maxsize

while inpt != 'Stop':
    num = int(inpt)
    if num > mxnum:
        mxnum = num
    inpt = input()

print(mxnum)
