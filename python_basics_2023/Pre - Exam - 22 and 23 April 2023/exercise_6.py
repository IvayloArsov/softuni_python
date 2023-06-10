n = input()

found = False  # initialize a variable to keep track of whether a valid combination is found

for a in range(1, 10):
    for b in range(9, a-1, -1):
        for c in range(0, 10):
            for d in range(9, c-1, -1):
                if (a + b + c + d) == (a * b * c * d) and int(n[-1]) == 5:
                    print(str(a) + str(b) + str(c) + str(d))
                    found = True
                    break  # stop the loops if the first condition is met
                if (a * b * c * d) // (a + b + c + d) == 3 and int(n) % 3 == 0:
                    print(str(d) + str(c) + str(b) + str(a))
                    found = True
                    break  # stop the loops if the second condition is met
            if found:
                break
        if found:
            break
    if found:
        break
else:
    print("Nothing found")