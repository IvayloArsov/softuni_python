def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)
        only_evens = [
            num for num in result
            if num % 2 == 0
        ]
        return only_evens

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
