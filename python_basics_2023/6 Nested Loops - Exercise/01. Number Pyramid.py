num = int(input())
counter = 1
checker = False
for row in range(1, num+1):
    for col in range(1, row+1):

        if counter > num:
            checker = True
            break
        print(str(counter)+ " ", end="")
        counter += 1
    if checker:
        break
    print()