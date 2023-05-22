def add_passengers(passengers):
    train[-1] += passengers

def insert_passengers(wagon, passengers):
    train[wagon] += passengers

def leave_passengers(wagon, passengers):
    train[wagon] -= passengers


train = [0 for _ in range(int(input()))]


while True:
    user_input = input().split()
    if user_input[0] == 'End':
        print(train)
        break
    elif user_input[0] == 'add':
        add_passengers(int(user_input[-1]))
    elif user_input[0] == 'insert':
        insert_passengers(int(user_input[1]), int(user_input[-1]))
    elif user_input[0] == 'leave':
        leave_passengers(int(user_input[1]), int(user_input[-1]))


# train = [0 for _ in range(int(input()))]
#
# while True:
#     command = input()
#     if command == 'End':
#         print(train)
#         break
#     elif command.startswith('add'):
#         command, number = command.split()
#         train[-1] += int(number)
#     elif command.startswith('insert'):
#         command, idx, number = command.split()
#         train[int(idx)] += int(number)
#     elif command.startswith('leave'):
#         command, idx, number = command.split()
#         train[int(idx)] -= int(number)


