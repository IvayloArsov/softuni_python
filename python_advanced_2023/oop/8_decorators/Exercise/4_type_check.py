def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    return "Bad Type"
            for key, value in kwargs.items():
                if not isinstance(value, expected_type):
                    return "Bad Type"
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
