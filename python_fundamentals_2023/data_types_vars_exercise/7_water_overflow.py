cap = 0
for i in range(int(input())):
    cmd = int(input())
    cap += cmd
    if cap > 255:
        print('Insufficient capacity!')
        cap -= cmd
print(cap)