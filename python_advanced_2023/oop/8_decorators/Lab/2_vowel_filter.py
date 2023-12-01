def vowel_filter(function):
    def wrapper():
        vowels = 'AaEeOoYyUu'
        result = function()
        only_vowels = [
            letter for letter in result
            if letter in vowels
        ]
        return only_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]



print(get_letters())
