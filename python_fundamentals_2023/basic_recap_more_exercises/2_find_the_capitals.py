word = input()

l = [
    i
    for i, char in enumerate(word)
    if char.isupper()
]
print(l)