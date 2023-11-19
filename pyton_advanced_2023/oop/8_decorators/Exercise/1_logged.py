def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_str = f'you called {func.__name__}{args}\nit returned {result}'
        return info_str
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
