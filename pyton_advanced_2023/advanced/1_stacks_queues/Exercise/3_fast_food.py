from collections import deque
stock = int(input())
orders = deque(map(int, input().split()))
biggest_order = max(orders)
print(biggest_order)

while orders:
    first_order = orders.popleft()
    if stock - first_order >= 0:
        stock -= first_order
    else:
        print(f"Orders left: {first_order}", *orders)
        break
else:
    print("Orders complete")