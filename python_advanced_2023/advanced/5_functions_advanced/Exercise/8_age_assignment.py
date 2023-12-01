def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        first_letter = name[0].upper()
        # if first_letter in kwargs.keys():
        age = kwargs[first_letter]
        result.append(f"{name} is {age} years old.")
    result.sort()
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
