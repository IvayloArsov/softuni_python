iters_ = int(input())

for _ in range(iters_):
    command = int(input())
    if command == 88:
        print('Hello')
    elif command == 86:
        print("How are you?")
    elif command > 88:
        print('Bye.')
    elif command < 88 and command != 88 or command != 86:
        print('GREAT!')