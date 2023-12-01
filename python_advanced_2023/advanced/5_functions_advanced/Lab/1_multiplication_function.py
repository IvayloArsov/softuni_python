def multiply(*args):
    if args:
        result = 1
        for num in args:
            result *= num
        return result

# def multiply(*args):
#     if len(args) == 0:
#         return 1
#     return args[0] * multiply(*args[1:])

