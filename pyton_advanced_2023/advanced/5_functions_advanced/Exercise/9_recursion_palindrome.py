def palindrome(word, index):
    end = len(word) - 1 - index
    if index >= end:
        return f"{word} is a palindrome"
    if word[index] == word[end]:
        return palindrome(word, index+1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
