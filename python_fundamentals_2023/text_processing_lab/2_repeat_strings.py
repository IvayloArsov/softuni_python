word = input().split()
result = ""
for w in word:
    length = len(w)
    result += w*length
print(result)