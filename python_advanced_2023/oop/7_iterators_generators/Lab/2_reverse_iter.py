class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.iterable[self.index]
            self.index -= 1
            return result
        raise StopIteration


def generator_func(start, end):
    for i in range(start, end):
        yield i


reversed_list = reverse_iter(generator_func(1, 6))
for item in reversed_list:
    print(item)
