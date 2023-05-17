i = list(range(1,11))
iterator = iter(i)
try:
    while True:
        print(next(iterator))
except StopIteration:
    pass