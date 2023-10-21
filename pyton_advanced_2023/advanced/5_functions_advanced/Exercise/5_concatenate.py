def concatenate(*args, **kwargs):
    result_string = "".join(args)
    for key, value in kwargs.items():
        result_string = result_string.replace(key, value)
    return result_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
