username = input()
password = input()
line = input()
while line != password:
    line = input()
print(f'Welcome {username}!')
