class store_results:
    def __init__(self, filename="results.txt"):
        self.filename = filename

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(self.filename, 'a') as file:
                file.write(f"Function {func.__name__} was called. Result: {result}\n")
            return result
        return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)


