text = input().split()
total_sum = 0
position = 0
for entry in text:
    first_letter = entry[0]
    last_letter = entry[-1]
    num = int(entry[1:-1])
    if first_letter.isupper():
        position = ord(first_letter)-64
        total_sum += num/position
    elif first_letter.islower():
        position = ord(first_letter)-96
        total_sum += num*position
    if last_letter.isupper():
        position = ord(last_letter)-64
        total_sum -= position
    elif last_letter.islower():
        position = ord(last_letter)-96
        total_sum += position
print(f"{total_sum:.2f}")