def prime_check(num):
    flag = False
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
        if flag:
            return False
        else:
            return True

print(prime_check(int(input())))