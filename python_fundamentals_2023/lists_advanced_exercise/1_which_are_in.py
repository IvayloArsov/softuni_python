sample_words = input().split(", ")
word_list = input().split(", ")


def find_substrings(sequence1, sequence2):
    return [str_1
            for str_1 in sequence1
            if any(str_1 in str_2
                   for str_2 in sequence2)]


substrings = find_substrings(sample_words, word_list)
print(substrings)
