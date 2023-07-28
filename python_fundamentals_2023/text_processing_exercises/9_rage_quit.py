text = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:  # text[index] is digit -> working with repetitions
        for next_symbols_index in range(index, len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)