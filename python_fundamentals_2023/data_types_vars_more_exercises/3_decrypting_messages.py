key_ = int(input())
str_ = []
for _ in range(int(input())):
    char = input()
    str_.append(chr(ord(char)+key_))

print("".join(str_))