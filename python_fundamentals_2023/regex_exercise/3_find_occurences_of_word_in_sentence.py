import re

sentence = input()
magic_word = input()

pattern = fr"\b{magic_word}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))
