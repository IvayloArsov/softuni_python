specials = [5,7,11]

for i in range(1, int(input())+1):
    sum_ = 0
    digits = i
    while digits >0:
        sum_ += digits%10
        digits=int(digits/10)
    if sum_ in specials:
        print(f"{i} -> True")
    else:
        print(f'{i} -> False')