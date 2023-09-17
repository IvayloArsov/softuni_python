from collections import deque

new_deq = deque()
while True:
    cmd = input()
    if cmd == "End":
        break

    new_deq.append(cmd)
    if cmd == "Paid":
        new_deq.pop()
        for _ in range(len(new_deq)):
            print(new_deq.popleft())


print(len(new_deq), "people remaining.")