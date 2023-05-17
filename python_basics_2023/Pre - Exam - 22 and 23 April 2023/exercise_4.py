days = int(input())

sum = 0
liters = 0

for rakia in range(days):
    quantity = float(input())
    degrees = float(input())

    sum += quantity*degrees
    liters += quantity

avg_deg = sum/liters
print(f"Liter: {liters:.2f}")
print(f"Degrees: {avg_deg:.2f}")
if avg_deg < 38:
    print("Not good, you should baking!")
if 38 <= avg_deg <= 42:
    print('Super!')
if avg_deg > 42:
    print("Dilution with distilled water!")
