from collections import deque

chocolate = [int(ch) for ch in input().split(", ")]
milk = deque(int(m) for m in input().split(", "))
milkshakes = 0

while chocolate and milk and milkshakes < 5:
    if chocolate[-1] <= 0 and milk[-1] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[-1] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        milkshakes += 1
    else:
        milk.rotate(-1)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocolate)) if chocolate else 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) if milk else 'empty'}")