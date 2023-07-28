sub = input()
big_string = input()
while sub in big_string:
    big_string = big_string.replace(sub, "")
print(big_string)