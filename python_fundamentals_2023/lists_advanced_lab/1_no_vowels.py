def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([char for char in string if char.lower() not in vowels])


user_input = input()
result = remove_vowels(user_input)
print(result)
