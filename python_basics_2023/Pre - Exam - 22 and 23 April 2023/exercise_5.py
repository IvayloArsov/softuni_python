end = 8848
start = 5364
days = 1

while True:
    sleep = input()

    if sleep == 'END':
        print("Failed!")
        print(f"{start}")
        break
    climbed = int(input())

    if sleep == 'Yes':
        days += 1
        start += climbed
    else:
        start += climbed
    if days > 5:
        start -= climbed

    if start >= end:
        print(f'Goal reached for {days} days!')
        break
    if days > 5:
        print("Failed!")
        print(f"{start}")
        break