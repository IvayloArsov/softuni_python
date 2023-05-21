numbers = input().split(' ')
words = list(input())

indices = []
for num in numbers:
    sum_ = 0
    for digit in num:
        sum_ += int(digit)

    indices.append(sum_)

new_string = ''
for index in indices:
    effective_index = index % len(words)
    new_string += words[effective_index]
    words.pop(effective_index)

print(new_string)
