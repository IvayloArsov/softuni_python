input_text = input()
info = sorted(list(input_text))
char_counts = {}

for char in info:
    char_counts[char] = char_counts.get(char, 0) + 1

for char, count in char_counts.items():
    print(f"{char}: {count} time/s")