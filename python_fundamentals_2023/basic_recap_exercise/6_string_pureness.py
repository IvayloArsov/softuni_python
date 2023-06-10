signs = ",._"
tries = int(input())

for _ in range(tries):
    str_ = input()

    membership = 0
    for char in str_:
        if char in signs:
            membership += 1
    if membership > 0:
        print(f"{str_} is not pure!")
    else:
        print(f'{str_} is pure.')