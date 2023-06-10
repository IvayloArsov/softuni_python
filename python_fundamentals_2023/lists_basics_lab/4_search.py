n = int(input())
magic_word = input()
all_list = []
filtered_list = []
for _ in range(n):
    sentence = input()
    all_list.append(sentence)
    if magic_word in sentence:
        filtered_list.append(sentence)

print(all_list)
print(filtered_list)
