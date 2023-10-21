lines = int(input())
lot = set()
for _ in range(lines):
    direction, reg_num = input().split(", ")
    if direction == "IN":
        lot.add(reg_num)
    elif direction == "OUT":
        lot.remove(reg_num)
if lot:
    print("\n".join(lot))
else:
    print("Parking Lot is Empty")