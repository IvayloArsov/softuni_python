months = int(input())
electricity = 0
water = 0
internet = 0
other = 0
total = 0

for i in range(0, months):
    tok = float(input())
    electricity += tok
    water += 20
    internet += 15
    other += (tok + 35)*1.2

total += electricity+water+internet+other

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {total/months:.2f} lv")
