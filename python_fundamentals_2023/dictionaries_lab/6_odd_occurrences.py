sequence = input().split()
dict_words = {}
for word in sequence:
    word_lower = word.lower()
    if word_lower not in dict_words:
        dict_words[word_lower] = 0
    dict_words[word_lower] += 1
for k, v in dict_words.items():
    if v % 2 != 0:
        print(k, end=' ')
        