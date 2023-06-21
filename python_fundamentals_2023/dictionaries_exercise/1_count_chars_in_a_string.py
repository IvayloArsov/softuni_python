characters = list(input())
count_dict = {
    char: characters.count(char)
    for char in characters
    if char != " "
}
for char, count in count_dict.items():
    print(f"{char} -> {count}")