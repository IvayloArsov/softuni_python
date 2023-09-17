from collections import deque

children = deque(input().split())
n = int(input())

while len(children) != 1:
    children.rotate(-(n-1))
    print("Removed", children.popleft())

print("Last is", children.popleft())