def cache(func):
    def wrapper(n):
        if not hasattr(wrapper, 'log'):
            wrapper.log = {}
        if n not in wrapper.log:
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)
print(fibonacci.log)