def number_increment(numbers):
    def increase():
        increment = [
            num + 1
            for num in numbers
        ]
        return increment
    return increase()


print(number_increment([1, 2, 3]))
