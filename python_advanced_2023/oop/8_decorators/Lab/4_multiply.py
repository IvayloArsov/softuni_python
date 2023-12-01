from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) * times
            return result

        return wrapper

    return decorator
# def multiply(times):
#     return lambda function: wraps(function)(lambda *args, **kwargs: function(*args, **kwargs) * times)
#

@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
