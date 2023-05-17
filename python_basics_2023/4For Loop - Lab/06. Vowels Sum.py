n = input().casefold()
sum_vowels = 0

for c in n:
    if c == 'a':
        sum_vowels += 1
    elif c == 'e':
        sum_vowels += 2
    elif c == 'i':
        sum_vowels += 3
    elif c == 'o':
        sum_vowels += 4
    elif c == 'u':
        sum_vowels += 5
print(sum_vowels)
