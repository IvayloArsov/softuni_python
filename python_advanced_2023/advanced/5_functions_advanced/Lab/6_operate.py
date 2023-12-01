from functools import reduce
def operate(operator, *args):
    def add():
        return sum(args)
        # return reduce(lambda a, b: a+b, args)
    def subtract():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result
    def multiply():
        result = 1
        for el in args:
            result *= el
        return result
    def divide():
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("/", 3, 4, 5))
